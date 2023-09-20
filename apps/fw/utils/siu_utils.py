from apps.fw.models.log_siu_model import LogSIU


def register_update(cantidad, origen):
    log_entry = LogSIU.objects.create(cantidad=cantidad, origen=origen)

    return log_entry
