from apps.fw.serializers.egreso_serializers import EgresoUpdateSerializer

from apps.fw.utils.universidad_utils import get_or_create_universidad
from apps.fw.utils.facultad_utils import get_or_create_facultad
from apps.fw.utils.carrera_utils import get_or_create_carrera


def check_or_transform_data(data):
    universidad = get_or_create_universidad(
        data=data["universidad"],
    )
    facultad = get_or_create_facultad(
        data=data["facultad"],
        universidad_id=universidad.id,
    )
    carrera = get_or_create_carrera(
        data=data["carrera"],
        facultad_id=facultad.id,
    )

    data_transformed = {
        "universidad": universidad.id,
        "facultad": facultad.id,
        "carrera": carrera.id,
        "usuario": data["usuario"],
        "ciclo_egreso": data["ciclo_egreso"],
        "matricula": data["matricula"],
        "postgrado": data["postgrado"],
    }

    return data_transformed


def create_egreso(carrera_id, usuario, ciclo_egreso):
    data_egreso = {
        "carrera": carrera_id,
        "usuario": usuario.id,
        "ciclo_egreso": ciclo_egreso,
    }
    serializer = EgresoUpdateSerializer(data=data_egreso)
    serializer.is_valid(raise_exception=True)
    egreso = serializer.save()
    return egreso
