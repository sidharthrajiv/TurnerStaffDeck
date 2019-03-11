from django.contrib import admin
from .models import Self
from .models import Manager
from .models import Peer
from .models import Partner

admin.site.register(Self)
admin.site.register(Manager)
admin.site.register(Peer)
admin.site.register(Partner)
