import os
from datetime import datetime as dt
WHITE_LIST= ['BTCUSDT', 'ETHUSDT', 'BCHUSDT', 'XRPUSDT', 'EOSUSDT', 'LTCUSDT', 'TRXUSDT',  'ETCUSDT',
             'LINKUSDT', 'XLMUSDT', 'ADAUSDT', 'XMRUSDT', 'DASHUSDT', 'ZECUSDT', 'XTZUSDT', 'BNBUSDT',
             'ATOMUSDT', 'ONTUSDT', 'IOTAUSDT', 'BATUSDT', 'VETUSDT', 'NEOUSDT', 'QTUMUSDT', 'IOSTUSDT',
             'THETAUSDT', 'ALGOUSDT', 'ZILUSDT', 'KNCUSDT', 'ZRXUSDT', 'COMPUSDT', 'OMGUSDT', 'DOGEUSDT',
             'SXPUSDT', 'KAVAUSDT', 'BANDUSDT', 'RLCUSDT', 'WAVESUSDT', 'MKRUSDT', 'SNXUSDT', 'DOTUSDT',
             'YFIUSDT', 'BALUSDT', 'CRVUSDT', 'TRBUSDT', 'RUNEUSDT', 'SUSHIUSDT',  'EGLDUSDT', 'SOLUSDT',
             'ICXUSDT', 'STORJUSDT', 'BLZUSDT', 'UNIUSDT', 'AVAXUSDT', 'FTMUSDT', 'ENJUSDT', 'FLMUSDT',
             'RENUSDT', 'KSMUSDT', 'NEARUSDT', 'AAVEUSDT', 'FILUSDT', 'RSRUSDT', 'LRCUSDT', 'MATICUSDT',
             'OCEANUSDT', 'BELUSDT', 'CTKUSDT', 'AXSUSDT', 'ALPHAUSDT', 'ZENUSDT', 'SKLUSDT', 'GRTUSDT',
             '1INCHUSDT', 'CHZUSDT', 'SANDUSDT', 'ANKRUSDT',  'LITUSDT', 'UNFIUSDT', 'REEFUSDT', 'RVNUSDT',
             'SFPUSDT', 'XEMUSDT',  'COTIUSDT', 'CHRUSDT', 'MANAUSDT', 'ALICEUSDT', 'HBARUSDT', 'ONEUSDT', 'LINAUSDT',
             'STMXUSDT', 'DENTUSDT', 'CELRUSDT', 'HOTUSDT', 'MTLUSDT', 'OGNUSDT', 'NKNUSDT',  'DGBUSDT',
             'BAKEUSDT', 'GTCUSDT',  'IOTXUSDT', 'AUDIOUSDT',  'C98USDT', 'MASKUSDT', 'ATAUSDT', 'DYDXUSDT',
             'GALAUSDT', 'CELOUSDT', 'ARUSDT', 'KLAYUSDT', 'ARPAUSDT', 'CTSIUSDT', 'LPTUSDT', 'ENSUSDT',
             'PEOPLEUSDT', 'ANTUSDT', 'ROSEUSDT', 'DUSKUSDT', 'FLOWUSDT', 'IMXUSDT', 'API3USDT', 'GMTUSDT',
             'APEUSDT', 'WOOUSDT', 'JASMYUSDT', 'DARUSDT', 'GALUSDT', 'OPUSDT', 'INJUSDT', 'STGUSDT','SPELLUSDT',
             'LDOUSDT', 'CVXUSDT', 'ICPUSDT', 'APTUSDT', 'QNTUSDT',  'FETUSDT', 'FXSUSDT', 'HOOKUSDT', 'MAGICUSDT',
             'RNDRUSDT', 'HIGHUSDT', 'MINAUSDT', 'ASTRUSDT', 'AGIXUSDT', 'PHBUSDT', 'GMXUSDT', 'CFXUSDT', 'STXUSDT',
             'BNXUSDT', 'ACHUSDT', 'SSVUSDT', 'CKBUSDT', 'PERPUSDT', 'TRUUSDT', 'LQTYUSDT', 'IDUSDT', 'ARBUSDT',
             'JOEUSDT', 'TLMUSDT', 'AMBUSDT', 'LEVERUSDT', 'RDNTUSDT', 'HFTUSDT', 'XVSUSDT',  'EDUUSDT', 'IDEXUSDT',
             'SUIUSDT', 'UMAUSDT', 'RADUSDT', 'KEYUSDT', 'COMBOUSDT', 'NMRUSDT','MAVUSDT', 'MDTUSDT',
             'XVGUSDT', 'WLDUSDT', 'PENDLEUSDT', 'ARKMUSDT', 'AGLDUSDT', 'YGGUSDT', 'BNTUSDT', 'OXTUSDT',
             'SEIUSDT',  'CYBERUSDT', 'HIFIUSDT', 'ARKUSDT', 'FRONTUSDT', 'GLMRUSDT', 'BICOUSDT',  'STRAXUSDT',
             'LOOMUSDT',  'BONDUSDT',  'STPTUSDT', 'WAXPUSDT',  'RIFUSDT', 'POLYXUSDT', 'GASUSDT', 'POWRUSDT',
             'SLPUSDT', 'TIAUSDT', 'SNTUSDT', 'CAKEUSDT', 'MEMEUSDT', 'TWTUSDT', 'ORDIUSDT', 'STEEMUSDT', 'BADGERUSDT']



# WHITE_LIST = ['BTCUSDT','ETHUSDT']

# для определения среднего обьема_______________
START_DATE = dt(2023, 1, 1).replace(hour=0, minute=0)
END_DATE = dt(2023, 11, 20)
# ______________________________________________

# стратегии______________________________________________

STRATEGY = [7,  10]
SYMBOL="BTCUSDT"



# для бектестинга_______________________________
# ______________________________________________
BASE_DIR=fr'D:\python\crypto\back_testing_db'
# путь до базы данных
NANE_DB='2023_futures_all'

# ______________________________________________


# версия приложения
VERSION = '0.0.1'
# автор приложния
AUTHOR = 'Khram_Ua and kaluga_sereu'
