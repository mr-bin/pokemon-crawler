from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_http_methods


@csrf_exempt
@require_http_methods(["POST"])
def sale_push(request, request_body, user, valid, timeout):
    """
    **Push car sale details**

    URL::

        http://<some-address>/push/

    METHOD::

        POST

    Parametrs:
        - **access_token** - string (required). User access_token

    Response:

        - 200:

            .. code-block:: js

                {"valid": "true"}

        - 400:

            No credentials in request

            .. code-block:: js

                {"error": "no credentials in request"}

        - 401:

            No credentials in request

            .. code-block:: js

                {"valid": "false"}
    """

    return JsonResponse({})
