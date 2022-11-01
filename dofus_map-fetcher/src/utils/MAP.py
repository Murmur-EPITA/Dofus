''' When we have empty maps '''
from src.maps.empty_amaknien import Amaknien
from src.maps.empty_ecaflipus import Ecaflipus
from src.maps.empty_enutrosor import Enutrosor
from src.maps.empty_incarnam import Incarnam
from src.maps.empty_srambad import Srambad
from src.maps.empty_xelorium import Xelorium

''' When we have filled maps '''
# from src.maps.Amaknien import Amaknien
# from src.maps.Ecaflipus import Ecaflipus
# from src.maps.Enutrosor import Enutrosor
# from src.maps.Incarnam import Incarnam
# from src.maps.Srambad import Srambad
# from src.maps.Xelorium import Xelorium


dofusMaps = {
    'Amaknien': Amaknien,
    'Incarnam': Incarnam,
    'Ecaflipus': Ecaflipus,
    'Enutrosor': Enutrosor,
    'Srambad': Srambad,
    'Xelorium': Xelorium
}
