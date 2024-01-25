from django.core.exceptions import ValidationError
from django.core.mail import send_mail
from django.http import HttpResponse
from django.shortcuts import render
from .models import NuevaOrden
from django.shortcuts import render, redirect
from django.contrib import messages


def nuevaorden_view(request):
    if request.method == "POST":
        nombre = request.POST.get("nombre")
        email = request.POST.get("email")
        service_type = request.POST.get("service-type")
        recurrente = request.POST.get("recurrente")
        volumen = request.POST.get("volumen")
        precio_factura = request.POST.get("precio_factura")
        numero_rastreo = request.POST.get("numero_rastreo")
        punto_de_carga = request.POST.get("puntoDeCarga")
        punto_de_descarga = request.POST.get("puntoDeDescarga")
        servicios_combinados = request.POST.getlist("servicios_combinados")
        tiempo_almacenamiento = request.POST.get("tiempo_almacenamiento")
        descripcion_mercancia = request.POST.get("descripcion_mercancia")
        factura = request.POST.get("factura")
        rfc = request.POST.get("rfc")
        # response_text = (
        #     f"Nombre: {nombre}, Email: {email}, Service Type: {service_type}, Recurrente: {recurrente}, "
        #     f"Volumen: {volumen}, Precio Factura: {precio_factura}, Numero Rastreo: {numero_rastreo}, "
        #     f"Punto de Carga: {punto_de_carga}, Punto de Descarga: {punto_de_descarga}, "
        #     f"Servicios Combinados: {servicios_combinados}, Tiempo Almacenamiento: {tiempo_almacenamiento}, "
        #     f"Descripción Mercancía: {descripcion_mercancia}, Factura: {factura}, RFC: {rfc}"
        # )
        orden = NuevaOrden(
            nombre=nombre,
            email=email,
            service_type=service_type,
            recurrente=recurrente,
            volumen=volumen,
            precio_factura=precio_factura,
            numero_rastreo=numero_rastreo,
            punto_de_carga=punto_de_carga,
            punto_de_descarga=punto_de_descarga,
            servicios_combinados=servicios_combinados,
            tiempo_almacenamiento=tiempo_almacenamiento,
            descripcion_mercancia=descripcion_mercancia,
            factura=factura,
            rfc=rfc,
        )

        # Save the instance to the database
        try:
            mail_subject = "Solicitud de cotización recibida"
            message = (
                "Estimado cliente,\n\n"
                "Gracias por su solicitud de cotización. Hemos recibido la siguiente información:\n\n"
                f"Nombre: {nombre}\n"
                f"Email: {email}\n"
                f"Tipo de servicio: {service_type}\n"
                f"Servicio recurrent: {recurrente}\n"
                f"Volumen: {volumen}\n"
                f"Precio de factura: {precio_factura}\n"
                f"Numero de rastreo: {numero_rastreo}\n"
                f"Punto de carga: {punto_de_carga}\n"
                f"Punto de descarga: {punto_de_descarga}\n"
                f"Servicios combinados: {servicios_combinados}\n"
                f"Tiempo de almacenamiento: {tiempo_almacenamiento}\n"
                f"Descripción de mercancia: {descripcion_mercancia}\n"
                f"Requiero factura: {factura}\n"
                f"RFC: {rfc}\n"
                # Include other fields as needed
                "\n\n"
                "Le informamos que estamos trabajando en su solicitud y que pronto recibirá una respuesta.\n\n"
                "Atentamente,\n"
                "Su equipo de soporte"
            )
            from_email = "info@correkaminos.com"  # Use your info email address
            to_email = [email]  # Use the customer's email address
            send_mail(mail_subject, message, from_email, to_email, fail_silently=False)
            orden.save()
            messages.success(request, "La orden se ha creado correctamente y se le enviará un correo electrónico.")
            return redirect('ordenregistrada')  # Replace 'home' with the actual name of your home URL pattern
        except ValidationError as e:
            # Handle validation errors (e.g., required fields missing)
            return HttpResponse(f"Validation Error: {str(e)}")
        except Exception as e:
            # Handle other exceptions (e.g., email sending failure)
            return HttpResponse(f"An error occurred: {str(e)}")

    return render(request, "ordenes/nuevaorden.html")

def ordenregistrada(request):
    return render(request, 'ordenes/ordenregistrada.html')