# # example/urls.py
# # from django.urls import path

# # from example.views import index


# # urlpatterns = [
# #     path('', index),
# # ]
# from django.contrib import admin
# from django.urls import path
# from example.views import *
# from django.contrib.staticfiles.urls import staticfiles_urlpatterns
# from django.conf import settings
# from django.conf.urls.static import static

# urlpatterns = [
#     path('',index),
#     path('documents/',documents,name="documents"),
#     path('register-page/',register_page,name="register_page"),
#     path('add-documents/',add_document,name="add_documents"),
#     path('login/',login_page,name="login_page"),
#     path('log-out/',log_out,name="log_out"),
#     path('delete/<id>/',delete_doc,name="delete_documents"),
#     path('update/<id>/',update_doc,name="update_documents")

# ]

# if settings.DEBUG:
#         urlpatterns += static(settings.MEDIA_URL,
#                               document_root=settings.MEDIA_ROOT)


# # urlpatterns += staticfiles_urlpatterns()