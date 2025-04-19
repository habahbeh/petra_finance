"""
ملف إعدادات مشروع نظام مالي لجامعة البترا
يحتوي على كافة الإعدادات اللازمة للنظام بما في ذلك دعم اللغتين العربية والإنجليزية
"""

import os
from pathlib import Path

# تحديد المسار الأساسي للمشروع
BASE_DIR = Path(__file__).resolve().parent.parent

# إعدادات الأمان - يجب تغييرها في بيئة الإنتاج
SECRET_KEY = 'django-insecure-change-this-in-production'

# وضع التطوير - يجب تعيينه إلى False في بيئة الإنتاج
DEBUG = True

ALLOWED_HOSTS = [*]

# تعريف التطبيقات المثبتة
INSTALLED_APPS = [
    # تطبيقات Django الأساسية
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    # مكتبات خارجية
    'bootstrap5',  # دعم Bootstrap 5
    'crispy_forms',  # لتنسيق النماذج
    'mptt',  # لدعم الهياكل الشجرية
    'modeltranslation',  # لدعم ترجمة النماذج

    # تطبيقات المشروع
    'accounts',
    'core',
    'budget',
    'projects',
    'scholarships',
    'conferences',
    'finance',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.locale.LocaleMiddleware',  # وسيط اللغات
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'petra_finance.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'django.template.context_processors.i18n',  # إضافة معالج سياق اللغات
            ],
        },
    },
]

WSGI_APPLICATION = 'petra_finance.wsgi.application'

# إعدادات قاعدة البيانات
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',  # يمكن تغييرها إلى postgresql أو sqlite3
        'NAME': 'research_fin',
        'USER': 'dbuser',  # تغيير هذا حسب إعدادات قاعدة البيانات
        'PASSWORD': 'dbpassword',  # تغيير هذا حسب إعدادات قاعدة البيانات
        'HOST': 'localhost',
        'PORT': '3306',
        'OPTIONS': {
            'charset': 'utf8mb4',
        }
    }
}

# التحقق من صحة كلمات المرور
AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]

# إعدادات المنطقة الزمنية واللغة
LANGUAGE_CODE = 'en'  # اللغة الافتراضية هي الإنجليزية كما طلبت

TIME_ZONE = 'Asia/Amman'  # المنطقة الزمنية للأردن

USE_I18N = True  # تفعيل دعم تعدد اللغات

USE_L10N = True  # تفعيل تنسيق الأرقام والتواريخ حسب اللغة

USE_TZ = True

# تعريف اللغات المتاحة
from django.utils.translation import gettext_lazy as _

LANGUAGES = [
    ('en', _('English')),
    ('ar', _('Arabic')),
]

# مسار ملفات الترجمة
LOCALE_PATHS = [
    os.path.join(BASE_DIR, 'locale'),
]

# معلومات المسارات الثابتة
STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'static'),
]

# مسار الوسائط المتعددة
MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

# إعدادات المستخدم الافتراضي
# AUTH_USER_MODEL = 'accounts.User'  # يمكن تفعيله إذا أردت استخدام نموذج مستخدم مخصص

# تعريف الصفحة الرئيسية بعد تسجيل الدخول
LOGIN_REDIRECT_URL = 'dashboard'
LOGOUT_REDIRECT_URL = 'login'
LOGIN_URL = 'login'

# إعدادات Crispy Forms
CRISPY_TEMPLATE_PACK = 'bootstrap5'

# تعريف نوع الحقل الأساسي
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'