# encoding: UTF-8
from __future__ import unicode_literals
HD_SERVER = 'ipc:///home/xchen/vt_historydata'

# 默认空值
EMPTY_STRING = ''
EMPTY_UNICODE = u''
EMPTY_INT = 0
EMPTY_FLOAT = 0.0
EMPTY_LONG = 0

# 方向常量
DIRECTION_NONE = u'无方向'
DIRECTION_LONG = u'多'
DIRECTION_SHORT = u'空'
DIRECTION_UNKNOWN = u'未知'
DIRECTION_NET = u'净'
DIRECTION_SELL = u'卖出'      # IB接口

# 开平常量
OFFSET_NONE = u'无开平'
OFFSET_OPEN = u'开仓'
OFFSET_CLOSE = u'平仓'
OFFSET_CLOSETODAY = u'平今'
OFFSET_CLOSEYESTERDAY = u'平昨'
OFFSET_UNKNOWN = u'未知'

# 状态常量
STATUS_NOTTRADED = u'未成交'
STATUS_PARTTRADED = u'部分成交'
STATUS_ALLTRADED = u'全部成交'
STATUS_CANCELLED = u'已撤销'
STATUS_UNKNOWN = u'未知'
STATUS_REJECTED = u'拒单'

# 合约类型常量
PRODUCT_EQUITY = u'股票'
PRODUCT_FUTURES = u'期货'
PRODUCT_BOND = u'债券'
PRODUCT_OPTION = u'期权'
PRODUCT_INDEX = u'指数'
PRODUCT_COMBINATION = u'组合'
PRODUCT_FOREX = u'外汇'
PRODUCT_UNKNOWN = u'未知'
PRODUCT_SPOT = u'现货'
PRODUCT_DEFER = u'延期'
PRODUCT_NONE = ''

# 价格类型常量
PRICETYPE_LIMITPRICE = u'限价'
PRICETYPE_MARKETPRICE = u'市价'
PRICETYPE_FAK = u'FAK'
PRICETYPE_FOK = u'FOK'
PRICETYPE_PRSPLIT = u'PRSPLIT'
PRICETYPE_VWAP = u'VWAP'
PRICETYPE_TWAP = u'TWAP'
PRICETYPE_BESTBIDASK = u'BESTBIDASK'
PRICETYPE_SMARTPRICE = u'SMARTPRICE'

# 期权类型
OPTION_CALL = u'看涨期权'
OPTION_PUT = u'看跌期权'

# 交易所类型
#EXCHANGE_SSE = 'SSE'       # 上交所
#EXCHANGE_SZSE = 'SZSE'     # 深交所
#EXCHANGE_CFFEX = 'CFFEX'   # 中金所
#EXCHANGE_SHFE = 'SHFE'     # 上期所
#EXCHANGE_CZCE = 'CZCE'     # 郑商所
#EXCHANGE_DCE = 'DCE'       # 大商所

EXCHANGE_SSE = 'SH'         # 上交所
EXCHANGE_SZSE = 'SZ'        # 深交所
EXCHANGE_CFFEX = 'CFE'      # 中金所
EXCHANGE_SHFE = 'SHF'       # 上期所
EXCHANGE_CZCE = 'CZC'       # 郑商所
EXCHANGE_DCE = 'DCE'        # 大商所
EXCHANGE_CSI = 'CSI'        # 中证指数
EXCHANGE_HKH = 'HKH'        # 沪港通
EXCHANGE_HKS = 'HKS'        # 深港通
EXCHANGE_JZ  = 'JZ'         # 均直
EXCHANGE_SPOT  = 'SPOT'     # 现货
EXCHANGE_IB  = 'IB'         # 银行间市场
EXCHANGE_FX  = 'FX'         # 外汇
EXCHANGE_INE  = 'INE'       # 能源

EXCHANGE_SGE = 'SGE'       # 上金所
EXCHANGE_UNKNOWN = 'UNKNOWN'# 未知交易所
EXCHANGE_NONE = ''          # 空交易所
EXCHANGE_HKEX = 'HKEX'      # 港交所

EXCHANGE_SMART = 'SMART'       # IB智能路由（股票、期权）
EXCHANGE_NYMEX = 'NYMEX'       # IB 期货
EXCHANGE_GLOBEX = 'GLOBEX'     # CME电子交易平台
EXCHANGE_IDEALPRO = 'IDEALPRO' # IB外汇ECN

EXCHANGE_CME = 'CME'           # CME交易所
EXCHANGE_ICE = 'ICE'           # ICE交易所

EXCHANGE_OANDA = 'OANDA'       # OANDA外汇做市商
EXCHANGE_OKCOIN = 'OKCOIN'     # OKCOIN比特币交易所

# 货币类型
CURRENCY_USD = 'USD'            # 美元
CURRENCY_CNY = 'CNY'            # 人民币
CURRENCY_UNKNOWN = 'UNKNOWN'    # 未知货币
CURRENCY_NONE = ''              # 空货币