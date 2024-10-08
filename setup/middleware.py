import logging

logger = logging.getLogger('custom')

class CustomMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response
    def __call__(self, request):
    # Código executado antes da view
        logger.info('Middleware executado: Interceptando requisição')
        if 'X-Meu-Header' in request.headers:
            
            request.session['meu_header'] = request.headers['X-Meu-Header']
            logger.info('Valor do cabeçalho armazenado na sessão: %s', request.session['meu_header'])
            response = self.get_response(request)
            logger.info('Middleware executado: Interceptando resposta')

            return response