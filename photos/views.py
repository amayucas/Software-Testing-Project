from django.http import HttpResponse
from photos.forms import PhotoForm
from photos.models import Photo, PUBLIC
from django.shortcuts import render
from django.http import HttpResponseNotFound
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.views.generic import View, ListView
from django.utils.decorators import method_decorator
from django.db.models import Q


class PhotosQueryset(object):

    def get_photos_queryset(self, request):
        if not request.user.is_authenticated:
            photos = Photo.objects.filter(visibility=PUBLIC)
        elif request.user.is_superuser:
            photos = Photo.objects.all()
        else:
            photos = Photo.objects.filter(Q(owner=request.user) | Q(visibility=PUBLIC))
        return photos


    def get_number_of_photos_from_user(self, request):
        number_of_photos = len(Photo.objects.filter(Q(owner=request.user)))
        return number_of_photos


class HomeView(View):

    def get(self, request):
        photos = Photo.objects.filter(visibility=PUBLIC).order_by('-created_at')
        context = {
            'photos_list': photos[:5]
        }
        return render(request, 'photos/home.html', context)


class DetailView(View, PhotosQueryset):
    def get(self, request, pk):
        """
        try:
            photo = Photo.objects.get(pk=pk)
        except Photo.DoesNotExist:
            photo = None
        except Photo.MultipleObjects:
            photo = None
        possible_photos = Photo.objects.filter(pk=pk)
        """
        possible_photos = self.get_photos_queryset(request).filter(pk=pk).select_related('owner')
        photo = possible_photos[0] if len(possible_photos) >= 1 else None
        if photo is not None:
            context = {
                'photo': photo
            }
            return render(request, 'photos/detail.html', context)
        else:
            return HttpResponseNotFound('La foto que estas buscando no existe')


class CreateView(View, PhotosQueryset):
    @method_decorator(login_required())
    def get(self, request):
        form = PhotoForm()
        number_of_photos_uploaded = self.get_number_of_photos_from_user(request)
        context = {
            'form': form,
            'success_message': '',
            'nof': number_of_photos_uploaded,
            'nof2': 25 - number_of_photos_uploaded
        }

        return render(request, 'photos/new_photo.html', context)

    @method_decorator(login_required())
    def post(self, request):
        success_message = ''
        number_of_photos_uploaded = self.get_number_of_photos_from_user(request)
        if not check_if_uploads_remaining(number_of_photos_uploaded):
            form = PhotoForm()
            success_message = 'Ya has subido 25 fotos. Has alcansado el limite.'
        else:
            photo_with_owner = Photo()
            photo_with_owner.owner = request.user
            form = PhotoForm(request.POST, instance=photo_with_owner)
            if form.is_valid():
                new_photo = form.save()
                form = PhotoForm()
                success_message = 'Guardado con éxito'
                success_message += '<br>'
                success_message += '<br>'
                success_message += '<a href="{0}">'.format(reverse('photos_detail', args=[new_photo.pk]))
                success_message += 'Ver foto'
                success_message += '</a>'
        context = {
            'form': form,
            'success_message': success_message,
            'nof': number_of_photos_uploaded,
            'nof2': 25-number_of_photos_uploaded
        }
        return render(request, 'photos/new_photo.html', context)


class PhotoListView(View, PhotosQueryset):
    def get(self, request):

        context = {
            'photos': self.get_photos_queryset(request)
        }
        return render(request, 'photos/photos_list.html', context)


class UserPhotosView(ListView):
    model = Photo
    template_name = 'photos/user_photos.html'

    def get_queryset(self):
        queryset = super(UserPhotosView, self).get_queryset()
        return queryset.filter(owner=self.request.user)


def check_if_uploads_remaining(number_of_uploaded_pictures):
    if type(number_of_uploaded_pictures) not in [int]:
        raise TypeError("The number of uploaded pictures must be a positive Integer")

    if number_of_uploaded_pictures < 0:
        raise ValueError("The number of uploaded pictures can't be negative")

    if number_of_uploaded_pictures >= 25:
        return False

    return True
