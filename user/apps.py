from django.apps import AppConfig

from django.db.models.signals import post_migrate




class UserConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'user'

    def initialize(self, signal, sender, app_config, **kwargs):
        userinfo = dict(username='admin', email='admin@gmail.com')
        User = app_config.get_model('User')

        if User.objects.filter(**userinfo).count() > 0:
            return

        admin = User(**userinfo, is_staff=True, is_superuser=True, is_active=True)
        admin.set_password('admin')
        admin.save()

    def ready(self):
        super().ready()
        post_migrate.connect(self.initialize, self)
