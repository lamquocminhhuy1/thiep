from django.shortcuts import render
from .models import WeddingInfo

def index(request):
    # Get the wedding info - assuming single instance logic from admin
    wedding_info = WeddingInfo.objects.first()
    
    # Fallback if not configured yet (or auto-create default)
    if not wedding_info:
        wedding_info = WeddingInfo.objects.create() # Uses defaults from model

    context = {
        'groom_name': wedding_info.groom_name,
        'bride_name': wedding_info.bride_name,
        'groom_parents_dad': wedding_info.groom_parents_dad,
        'groom_parents_mom': wedding_info.groom_parents_mom,
        'bride_parents_dad': wedding_info.bride_parents_dad,
        'bride_parents_mom': wedding_info.bride_parents_mom,
        'groom_address': wedding_info.groom_address,
        'bride_address': wedding_info.bride_address,
        'ceremony_date_short': wedding_info.ceremony_date_str.split(',')[1].strip() if ',' in wedding_info.ceremony_date_str else wedding_info.ceremony_date_str, # Simple parse or just use str
        'ceremony_days_until': '00', # Placeholder for countdown logic if needed
        # Pass the whole object for easier access in template
        'wedding_info': wedding_info,
        
        # Mapping old context keys to new model fields for compatibility
        'ceremony_time': wedding_info.ceremony_time_str,
        'ceremony_date': wedding_info.ceremony_date_str,
        'reception_time': wedding_info.reception_time_str,
        'reception_date': wedding_info.reception_date_str,
        'google_map_link': wedding_info.google_map_link,
        'album_photos': wedding_info.album_photos.all(),
    }
    return render(request, 'invitation/index.html', context)

def bride_side(request):
    # Get the wedding info - assuming single instance logic from admin
    wedding_info = WeddingInfo.objects.first()
    
    # Fallback if not configured yet (or auto-create default)
    if not wedding_info:
        wedding_info = WeddingInfo.objects.create() # Uses defaults from model

    context = {
        'groom_name': wedding_info.groom_name,
        'bride_name': wedding_info.bride_name,
        'groom_parents_dad': wedding_info.groom_parents_dad,
        'groom_parents_mom': wedding_info.groom_parents_mom,
        'bride_parents_dad': wedding_info.bride_parents_dad,
        'bride_parents_mom': wedding_info.bride_parents_mom,
        'groom_address': wedding_info.groom_address,
        'bride_address': wedding_info.bride_address,
        'ceremony_date_short': wedding_info.ceremony_date_str.split(',')[1].strip() if ',' in wedding_info.ceremony_date_str else wedding_info.ceremony_date_str, # Simple parse or just use str
        'ceremony_days_until': '00', # Placeholder for countdown logic if needed
        # Pass the whole object for easier access in template
        'wedding_info': wedding_info,
        
        # Mapping old context keys to new model fields for compatibility
        'ceremony_time': wedding_info.ceremony_time_str,
        'ceremony_date': wedding_info.ceremony_date_str,
        'reception_time': wedding_info.reception_time_str,
        'reception_date': wedding_info.reception_date_str,
        'google_map_link': wedding_info.google_map_link,
        'album_photos': wedding_info.album_photos.all(),
    }
    return render(request, 'invitation/index_bride.html', context)
