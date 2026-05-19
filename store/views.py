from django.shortcuts import render, redirect
from django.contrib import messages
from django.conf import settings
from django.http import JsonResponse
from django.views.decorators.http import require_POST
import cloudinary.uploader
from .models import ProductImage, CATEGORY_CHOICES

CATEGORY_INFO = {
    'tshirts': {
        'name': 'T-Shirts',
        'icon': '👕',
        'description': 'Premium export surplus t-shirts from top international brands. Round neck, polo, printed & plain styles.',
        'banner_color': '#1a1a2e',
    },
    'trackpants': {
        'name': 'Track Pants',
        'icon': '👖',
        'description': 'Comfortable export surplus track pants. Perfect for sports, gym, and casual wear.',
        'banner_color': '#16213e',
    },
    'shorts': {
        'name': 'Shorts',
        'icon': '🩳',
        'description': 'Stylish export surplus shorts for all occasions - beach, sports, and casual outings.',
        'banner_color': '#0f3460',
    },
    'hoodies': {
        'name': 'Hoodies',
        'icon': '🧥',
        'description': 'Warm & cozy export surplus hoodies and sweatshirts from premium international brands.',
        'banner_color': '#533483',
    },
    'babies': {
        'name': 'Born Babies Garments',
        'icon': '👶',
        'description': 'Soft, safe, and adorable export surplus baby garments for newborns to toddlers.',
        'banner_color': '#e94560',
    },
}

def home(request):
    featured_images = ProductImage.objects.filter(is_featured=True)[:8]
    categories = [(k, v) for k, v in CATEGORY_INFO.items()]
    return render(request, 'store/home.html', {
        'featured_images': featured_images,
        'categories': categories,
    })

def product_category(request, category):
    if category not in CATEGORY_INFO:
        return redirect('home')
    images = ProductImage.objects.filter(category=category)
    info = CATEGORY_INFO[category]
    return render(request, 'store/category.html', {
        'category': category,
        'info': info,
        'images': images,
        'all_categories': CATEGORY_INFO,
    })

def contact(request):
    return render(request, 'store/contact.html')

def about(request):
    return render(request, 'store/about.html')

# ── Admin Panel ──────────────────────────────────────────────────────────────

def admin_login(request):
    if request.session.get('admin_logged_in'):
        return redirect('admin_dashboard')
    
    if request.method == 'POST':
        username = request.POST.get('username', '')
        password = request.POST.get('password', '')
        if username == settings.ADMIN_USERNAME and password == settings.ADMIN_PASSWORD:
            request.session['admin_logged_in'] = True
            return redirect('admin_dashboard')
        else:
            messages.error(request, 'Invalid username or password.')
    
    return render(request, 'store/admin_login.html')

def admin_logout(request):
    request.session.flush()
    return redirect('admin_login')

def admin_dashboard(request):
    if not request.session.get('admin_logged_in'):
        return redirect('admin_login')

    images = ProductImage.objects.all().order_by('-uploaded_at')

    ICONS = {'tshirts': '👕', 'trackpants': '👖', 'shorts': '🩳', 'hoodies': '🧥', 'babies': '👶'}
    categories_with_counts = [
        (cat, label, ProductImage.objects.filter(category=cat).count(), ICONS.get(cat, '📦'))
        for cat, label in CATEGORY_CHOICES
    ]

    return render(request, 'store/admin_dashboard.html', {
        'images': images,
        'categories': CATEGORY_CHOICES,
        'categories_with_counts': categories_with_counts,
        'total': images.count(),
    })

@require_POST
def admin_upload(request):
    if not request.session.get('admin_logged_in'):
        return JsonResponse({'error': 'Unauthorized'}, status=401)
    
    files = request.FILES.getlist('images')
    category = request.POST.get('category')
    title = request.POST.get('title', '')
    description = request.POST.get('description', '')
    is_featured = request.POST.get('is_featured') == 'on'
    
    if not files or not category:
        messages.error(request, 'Please select images and a category.')
        return redirect('admin_dashboard')
    
    uploaded = 0
    for f in files:
        try:
            result = cloudinary.uploader.upload(f, folder=f'ajai_pranav_tex/{category}')
            ProductImage.objects.create(
                category=category,
                image=result['public_id'],
                title=title,
                description=description,
                is_featured=is_featured,
            )
            uploaded += 1
        except Exception as e:
            messages.error(request, f'Failed to upload {f.name}: {str(e)}')
    
    if uploaded:
        messages.success(request, f'Successfully uploaded {uploaded} image(s)!')
    return redirect('admin_dashboard')

@require_POST
def admin_delete(request, image_id):
    if not request.session.get('admin_logged_in'):
        return JsonResponse({'error': 'Unauthorized'}, status=401)
    
    try:
        img = ProductImage.objects.get(id=image_id)
        # Delete from Cloudinary
        try:
            cloudinary.uploader.destroy(str(img.image))
        except:
            pass
        img.delete()
        messages.success(request, 'Image deleted successfully.')
    except ProductImage.DoesNotExist:
        messages.error(request, 'Image not found.')
    
    return redirect('admin_dashboard')

@require_POST  
def admin_toggle_featured(request, image_id):
    if not request.session.get('admin_logged_in'):
        return JsonResponse({'error': 'Unauthorized'}, status=401)
    try:
        img = ProductImage.objects.get(id=image_id)
        img.is_featured = not img.is_featured
        img.save()
        messages.success(request, f'Image {"featured" if img.is_featured else "unfeatured"} successfully.')
    except ProductImage.DoesNotExist:
        messages.error(request, 'Image not found.')
    return redirect('admin_dashboard')
