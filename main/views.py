from django.views.generic import TemplateView, View
from django.http import JsonResponse
from qiniu import Auth


class HomepageView(TemplateView):
    template_name = 'main/index.html'

    def get_context_data(self, **kwargs):
        ctx = super(HomepageView, self).get_context_data(**kwargs)
        ctx['uptoken_url'] = '/token/'
        ctx['domain'] = 'YOUR_BUCKET_DOMAIN'
        return ctx


class TokenView(View):
    def get(self, request, *args, **kwargs):
        access_key = 'YOUR_ACCESS_KEY'
        secret_key = 'YOUR_SECRET_KEY'
        bucket_name = 'YOUR_BUCKET_NAME'

        auth = Auth(access_key, secret_key)
        token = auth.upload_token(bucket_name)
        return JsonResponse({'uptoken': token})
