import requests
from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic import TemplateView
from pusher import Pusher
import requests
import json

pusher = Pusher(app_id=u"797292", key=u"e696b02fe8b71c18956d", secret=u"abe757f2dd41ffdfad95", cluster=u"us2")


class PainelTemplate(TemplateView):
    template_name = 'templates/demo1/dist/layout/general/index.html'
    fields = '__all__'

    def get_sessoes(self):
        sessoes = requests.get('https://admin.intellgest.com.br/app/sessoes/')
        sessoes = json.loads(sessoes.content)
        return sessoes['clientes-em-sessao']

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['sessoes'] = self.get_sessoes()
        return context

