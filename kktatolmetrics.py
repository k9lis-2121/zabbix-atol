# -*- coding: utf-8 -*-
import sys
from libfptr10 import IFptr
import datetime
import time
import json
import os

fptr = IFptr("")

fptr.setSingleSetting(IFptr.LIBFPTR_SETTING_PORT, str(IFptr.LIBFPTR_PORT_USB))
fptr.applySingleSettings()

i = 1
while i < 10:
    fptr.open()
    if fptr.isOpened():
        print('Connetciont true')
        i = 10
    else:
            time.sleep(2)
            #i = i + i
            print('Connetciont...')

def deltadate(paramAsDateTime):
	now = datetime.datetime.now()
	deltaindays = (paramAsDateTime - now).days
	if deltaindays < -10000:
		return 0
	else:
		return deltaindays + 1
        
        
print(sys.argv)




for i in sys.argv:

    if i == 'reboot':
        print(str(i))
        print('rebooting...')
        #fptr.setParam(IFptr.LIBFPTR_PARAM_PRINT_REPORT, False)
        fptr.deviceReboot()
        fptr.beep()
        fptr.beep()

#SerNKKT                        - Заводской номер ККТ
#RegNKKT                        - Рег. № ККТ
#SerNFN                         - серийный номер ФН
#FNdeadline                     - дней до конца срока фн
#AgeDaysFirstDontSendDocInFN    - Возраст в днях первого не отправленного документа в ФН
#ModelKKT                       - Модель ККТ
#MicroProgramVer                - Версия прошивки
#isPaperPresent                 - Наличие бумаги
#isPaperNearEnd                 - Заканчивается ли бумага
#isCoverOpened                  - Состояние крышки
#ShiftState                     - Состояние смены
#NomberShift                    - Номер смены
#DateCloseShift                 - Дата закрытия смены
#ErrNoSerialNumber              - Не введн ЗН ККТ
#ErrRtcFault                    - Ошибка часов реального времени
#ErrSettings                    - Ошибка в настройках
#ErrCounterFault                - Ошибка счетчиков
#ErrUserMemoryFault             - Ошибка пользовательской памяти
#ErrServiceCountersFault        - Ошибка сервисных регистров
#ErrAttributesFault             - Ошибка реквизитов
#ErrFnFault                     - Фатальная ошибка ФН
#ErrInvalidFN                   - Установлен ФН из другой ККТ
#ErrHardFault                   - Фатальная аппаратная ошибка
#ErrMemoryManagerFault          - Ошибка диспетчера памяти
#ErrScriptFault                 - Шаблоны повреждены или отсутствуют
#ErrWaitForReboot               - Требуется перезагрузка
#ErrUniversalCountersFault      - Ошибка унивесальных счетчиков
#UptimeKKTSec                   - Uptime
#DateTimeLastSendToOFD          - Последняя отправка в ОФД

#1060	Адрес сайта ФНС	string
#1009	Адрес расчетов	string
#1018	ИНН организации	string
#1048	Название организации	string
#1062	Системы налогообложения	int
#1117	E-mail организации	string
#1057	Признак агента	int
#1187	Адрес места расчетов	string
#1037	Регистрационный номер устройства	string
#1209	Версия ФФД	int
#1001	Признак автоматического режима	bool
#1036	Номер автомата	string
#1002	Признак автономного режима	bool
#1056	Признак шифрования	bool
#1108	Признак ККТ для расчетов в сети Интернет	bool
#1109	Признак расчетов за услуги	bool
#1110	Признак АС БСО	bool
#1126	Признак проведения лотерей	bool
#1193	Признак проведения азартных игр	bool
#1207	Признак подакцизного товара	bool
#1221	Признак установки принтера в автомате	bool
#1017	ИНН ОФД	string
#1046	Название ОФД	string     
#exchangeStatus                 - Статус информационного обмена с ОФД  (0 - транспортное соединение установлено
#                                                                       1 - есть сообщение для передачи в ОФД
#                                                                       2 - ожидание ответного сообщения (квитанции) от ОФД
#                                                                       3 - есть команда от ОФД
#                                                                       4 - тизменились настройки соединения с ОФД
#                                                                       5 - ожидание ответа на команду от ОФД)
#unsentCount                    - Количество не отправленных документов
#ofdMessageRead                 - Дата и время первого Не отправленного документа
#fnNeedReplacement              - Требуется срочная замена ФН
#fnExhausted                    - Исчерпан ресурс ФН
#fnMemoryOverflow               - Память ФН переполнена
#fnCriticalError                - Критическая ошибка ФН
#daysRemain                     - Осталось рабочих дней ФН
#ErrFNNetworkErrorText          - Текст ошибки сети
#ErrFNOfdErrorText              - Текст ошибки ОФД
#ErrFNFnErrorText               - Текст ошибки ФН
#ErrFNDocumentNumber            - Номер документа на котором произошла ошибка
#ErrFNCommandCode               - Команда ФН на которой произошла ошибка
#ErrFNDateTime                  - Дата и время последнего успешного соединение
#

#SerNKKT RegNKKT SerNFN FNdeadline AgeDaysFirstDontSendDocInFN ModelKKT MicroProgramVer isPaperPresent isPaperNearEnd isCoverOpened ShiftState NomberShift DateCloseShift ErrNoSerialNumber ErrSettings ErrCounterFault ErrUserMemoryFault ErrServiceCountersFault ErrAttributesFault ErrFnFault ErrInvalidFN ErrHardFault ErrMemoryManagerFault ErrScriptFault ErrWaitForReboot ErrUniversalCountersFault UptimeKKTSec DateTimeLastSendToOFD 1060 1009 1018 1048 1062 1117 1057 1187 1037 1037 1209 1001 1036 1002 1056 1108 1109 1110 1126 1193 1193 1207 1221 1017 1046 exchangeStatus unsentCount ofdMessageRead fnNeedReplacement fnExhausted fnMemoryOverflow fnCriticalError daysRemain ErrFNNetworkErrorText ErrFNOfdErrorText ErrFNFnErrorText ErrFNDocumentNumber ErrFNCommandCode ErrFNDateTime

print('givenstarts')

fptr.setParam(IFptr.LIBFPTR_PARAM_FN_DATA_TYPE, IFptr.LIBFPTR_FNDT_VALIDITY)
fptr.fnQueryData()
SerNKKT = deltadate(fptr.getParamDateTime(IFptr.LIBFPTR_PARAM_DATE_TIME))
    
fptr.setParam(IFptr.LIBFPTR_PARAM_DATA_TYPE, IFptr.LIBFPTR_DT_SERIAL_NUMBER)
fptr.queryData()
RegNKKT = fptr.getParamString(IFptr.LIBFPTR_PARAM_SERIAL_NUMBER)

fptr.setParam(IFptr.LIBFPTR_PARAM_FN_DATA_TYPE, IFptr.LIBFPTR_FNDT_FN_INFO)
fptr.fnQueryData()
SerNFN = fptr.getParamString(IFptr.LIBFPTR_PARAM_SERIAL_NUMBER)
        
fptr.setParam(IFptr.LIBFPTR_PARAM_FN_DATA_TYPE, IFptr.LIBFPTR_FNDT_VALIDITY)
fptr.fnQueryData()
FNdeadline = deltadate(fptr.getParamDateTime(IFptr.LIBFPTR_PARAM_DATE_TIME))
        
fptr.setParam(IFptr.LIBFPTR_PARAM_FN_DATA_TYPE, IFptr.LIBFPTR_FNDT_OFD_EXCHANGE_STATUS)
fptr.fnQueryData()
AgeDaysFirstDontSendDocInFN = deltadate(fptr.getParamDateTime(IFptr.LIBFPTR_PARAM_DATE_TIME))*(-1)
        
fptr.setParam(IFptr.LIBFPTR_PARAM_DATA_TYPE, IFptr.LIBFPTR_DT_STATUS)
fptr.queryData()
ModelKKT = fptr.getParamString(IFptr.LIBFPTR_PARAM_MODEL_NAME)
        
fptr.setParam(IFptr.LIBFPTR_PARAM_DATA_TYPE, IFptr.LIBFPTR_DT_STATUS)
fptr.queryData()
MicroProgramVer = fptr.getParamString(IFptr.LIBFPTR_PARAM_UNIT_VERSION)
        
fptr.setParam(IFptr.LIBFPTR_PARAM_DATA_TYPE, IFptr.LIBFPTR_DT_SHORT_STATUS)
fptr.queryData()
isPaperPresent = fptr.getParamBool(IFptr.LIBFPTR_PARAM_RECEIPT_PAPER_PRESENT)
        
fptr.setParam(IFptr.LIBFPTR_PARAM_DATA_TYPE, IFptr.LIBFPTR_DT_SHORT_STATUS)
fptr.queryData()
isPaperNearEnd = fptr.getParamBool(IFptr.LIBFPTR_PARAM_PAPER_NEAR_END)
        
fptr.setParam(IFptr.LIBFPTR_PARAM_DATA_TYPE, IFptr.LIBFPTR_DT_SHORT_STATUS)
fptr.queryData()
isCoverOpened = fptr.getParamBool(IFptr.LIBFPTR_PARAM_COVER_OPENED)
        
fptr.setParam(IFptr.LIBFPTR_PARAM_DATA_TYPE, IFptr.LIBFPTR_DT_SHIFT_STATE)
fptr.queryData()
ShiftState = fptr.getParamInt(IFptr.LIBFPTR_PARAM_SHIFT_STATE)
    
fptr.setParam(IFptr.LIBFPTR_PARAM_DATA_TYPE, IFptr.LIBFPTR_DT_SHIFT_STATE)
fptr.queryData()
NomberShift = fptr.getParamInt(IFptr.LIBFPTR_PARAM_SHIFT_NUMBER)
        
fptr.setParam(IFptr.LIBFPTR_PARAM_DATA_TYPE, IFptr.LIBFPTR_DT_SHIFT_STATE)
fptr.queryData()
DateCloseShift = fptr.getParamDateTime(IFptr.LIBFPTR_PARAM_DATE_TIME)
        
fptr.setParam(IFptr.LIBFPTR_PARAM_DATA_TYPE, IFptr.LIBFPTR_DT_FATAL_STATUS)
fptr.queryData()
ErrNoSerialNumber = fptr.getParamBool(IFptr.LIBFPTR_PARAM_NO_SERIAL_NUMBER)
        
fptr.setParam(IFptr.LIBFPTR_PARAM_DATA_TYPE, IFptr.LIBFPTR_DT_FATAL_STATUS)
fptr.queryData()
ErrRtcFault = fptr.getParamBool(IFptr.LIBFPTR_PARAM_RTC_FAULT)
        
fptr.setParam(IFptr.LIBFPTR_PARAM_DATA_TYPE, IFptr.LIBFPTR_DT_FATAL_STATUS)
fptr.queryData()
ErrSettings = fptr.getParamBool(IFptr.LIBFPTR_PARAM_SETTINGS_FAULT)
        
fptr.setParam(IFptr.LIBFPTR_PARAM_DATA_TYPE, IFptr.LIBFPTR_DT_FATAL_STATUS)
fptr.queryData()
ErrCounterFault = fptr.getParamBool(IFptr.LIBFPTR_PARAM_COUNTERS_FAULT)
        
fptr.setParam(IFptr.LIBFPTR_PARAM_DATA_TYPE, IFptr.LIBFPTR_DT_FATAL_STATUS)
fptr.queryData()
ErrUserMemoryFault = fptr.getParamBool(IFptr.LIBFPTR_PARAM_USER_MEMORY_FAULT)
        
fptr.setParam(IFptr.LIBFPTR_PARAM_DATA_TYPE, IFptr.LIBFPTR_DT_FATAL_STATUS)
fptr.queryData()
ErrServiceCountersFault = fptr.getParamBool(IFptr.LIBFPTR_PARAM_SERVICE_COUNTERS_FAULT)
        
fptr.setParam(IFptr.LIBFPTR_PARAM_DATA_TYPE, IFptr.LIBFPTR_DT_FATAL_STATUS)
fptr.queryData()
ErrAttributesFault = fptr.getParamBool(IFptr.LIBFPTR_PARAM_ATTRIBUTES_FAULT)
        
fptr.setParam(IFptr.LIBFPTR_PARAM_DATA_TYPE, IFptr.LIBFPTR_DT_FATAL_STATUS)
fptr.queryData()
ErrFnFault = fptr.getParamBool(IFptr.LIBFPTR_PARAM_FN_FAULT)
        
fptr.setParam(IFptr.LIBFPTR_PARAM_DATA_TYPE, IFptr.LIBFPTR_DT_FATAL_STATUS)
fptr.queryData()
ErrInvalidFN = fptr.getParamBool(IFptr.LIBFPTR_PARAM_INVALID_FN)
        
fptr.setParam(IFptr.LIBFPTR_PARAM_DATA_TYPE, IFptr.LIBFPTR_DT_FATAL_STATUS)
fptr.queryData()
ErrHardFault = fptr.getParamBool(IFptr.LIBFPTR_PARAM_HARD_FAULT)
        
fptr.setParam(IFptr.LIBFPTR_PARAM_DATA_TYPE, IFptr.LIBFPTR_DT_FATAL_STATUS)
fptr.queryData()
ErrMemoryManagerFault = fptr.getParamBool(IFptr.LIBFPTR_PARAM_MEMORY_MANAGER_FAULT)
    
fptr.setParam(IFptr.LIBFPTR_PARAM_DATA_TYPE, IFptr.LIBFPTR_DT_FATAL_STATUS)
fptr.queryData()
ErrScriptFault = fptr.getParamBool(IFptr.LIBFPTR_PARAM_SCRIPTS_FAULT)
        
fptr.setParam(IFptr.LIBFPTR_PARAM_DATA_TYPE, IFptr.LIBFPTR_DT_FATAL_STATUS)
fptr.queryData()
ErrWaitForReboot = fptr.getParamBool(IFptr.LIBFPTR_PARAM_WAIT_FOR_REBOOT)
        
fptr.setParam(IFptr.LIBFPTR_PARAM_DATA_TYPE, IFptr.LIBFPTR_DT_FATAL_STATUS)
fptr.queryData()
ErrUniversalCountersFault = fptr.getParamBool(IFptr.LIBFPTR_PARAM_UNIVERSAL_COUNTERS_FAULT)
        
fptr.setParam(IFptr.LIBFPTR_PARAM_DATA_TYPE, IFptr.LIBFPTR_DT_DEVICE_UPTIME)
fptr.queryData()
uptime = fptr.getParamInt(IFptr.LIBFPTR_PARAM_DEVICE_UPTIME)
        
fptr.setParam(IFptr.LIBFPTR_PARAM_DATA_TYPE, IFptr.LIBFPTR_DT_LAST_SENT_OFD_DOCUMENT_DATE_TIME)
fptr.queryData()
dateTimeOfd = fptr.getParamDateTime(IFptr.LIBFPTR_PARAM_DATE_TIME)
DateTimeLastSendToOFD = dateTimeOfd

fptr.setParam(IFptr.LIBFPTR_PARAM_FN_DATA_TYPE, IFptr.LIBFPTR_FNDT_OFD_EXCHANGE_STATUS)
fptr.fnQueryData()
exchangeStatus = fptr.getParamInt(IFptr.LIBFPTR_PARAM_OFD_EXCHANGE_STATUS)
        
fptr.setParam(IFptr.LIBFPTR_PARAM_FN_DATA_TYPE, IFptr.LIBFPTR_FNDT_OFD_EXCHANGE_STATUS)
fptr.fnQueryData()
unsentCount = fptr.getParamInt(IFptr.LIBFPTR_PARAM_DOCUMENTS_COUNT)
     
fptr.setParam(IFptr.LIBFPTR_PARAM_FN_DATA_TYPE, IFptr.LIBFPTR_FNDT_OFD_EXCHANGE_STATUS)
fptr.fnQueryData()
ofdMessageRead = fptr.getParamBool(IFptr.LIBFPTR_PARAM_OFD_MESSAGE_READ)
        
fptr.setParam(IFptr.LIBFPTR_PARAM_FN_DATA_TYPE, IFptr.LIBFPTR_FNDT_FN_INFO)
fptr.fnQueryData()
fnNeedReplacement = fptr.getParamBool(IFptr.LIBFPTR_PARAM_FN_NEED_REPLACEMENT)
        
fptr.setParam(IFptr.LIBFPTR_PARAM_FN_DATA_TYPE, IFptr.LIBFPTR_FNDT_FN_INFO)
fptr.fnQueryData()
fnExhausted = fptr.getParamBool(IFptr.LIBFPTR_PARAM_FN_RESOURCE_EXHAUSTED)
        
fptr.setParam(IFptr.LIBFPTR_PARAM_FN_DATA_TYPE, IFptr.LIBFPTR_FNDT_FN_INFO)
fptr.fnQueryData()
fnMemoryOverflow = fptr.getParamBool(IFptr.LIBFPTR_PARAM_FN_MEMORY_OVERFLOW)
        
fptr.setParam(IFptr.LIBFPTR_PARAM_FN_DATA_TYPE, IFptr.LIBFPTR_FNDT_FN_INFO)
fptr.fnQueryData()
fnCriticalError = fptr.getParamBool(IFptr.LIBFPTR_PARAM_FN_CRITICAL_ERROR)
        
fptr.setParam(IFptr.LIBFPTR_PARAM_DATA_TYPE, IFptr.LIBFPTR_DT_DATE_TIME)
fptr.queryData()
dateTime = fptr.getParamDateTime(IFptr.LIBFPTR_PARAM_DATE_TIME)
fptr.setParam(IFptr.LIBFPTR_PARAM_FN_DATA_TYPE, IFptr.LIBFPTR_FNDT_VALIDITY_DAYS)
fptr.setParam(IFptr.LIBFPTR_PARAM_DATE_TIME, dateTime)
fptr.fnQueryData()
daysRemain = fptr.getParamInt(IFptr.LIBFPTR_PARAM_FN_DAYS_REMAIN)
        
fptr.setParam(IFptr.LIBFPTR_PARAM_FN_DATA_TYPE, IFptr.LIBFPTR_FNDT_ERRORS)
fptr.fnQueryData()
ErrFNNetworkErrorText = fptr.getParamString(IFptr.LIBFPTR_PARAM_NETWORK_ERROR_TEXT)
        
        
fptr.setParam(IFptr.LIBFPTR_PARAM_FN_DATA_TYPE, IFptr.LIBFPTR_FNDT_ERRORS)
fptr.fnQueryData()
ErrFNOfdErrorText = fptr.getParamString(IFptr.LIBFPTR_PARAM_OFD_ERROR_TEXT)
        
fptr.setParam(IFptr.LIBFPTR_PARAM_FN_DATA_TYPE, IFptr.LIBFPTR_FNDT_ERRORS)
fptr.fnQueryData()
ErrFNFnErrorText = fptr.getParamString(IFptr.LIBFPTR_PARAM_FN_ERROR_TEXT)
        
fptr.setParam(IFptr.LIBFPTR_PARAM_FN_DATA_TYPE, IFptr.LIBFPTR_FNDT_ERRORS)
fptr.fnQueryData()
ErrFNDocumentNumber = fptr.getParamInt(IFptr.LIBFPTR_PARAM_DOCUMENT_NUMBER)
        
fptr.setParam(IFptr.LIBFPTR_PARAM_FN_DATA_TYPE, IFptr.LIBFPTR_FNDT_ERRORS)
fptr.fnQueryData()
ErrFNCommandCode = fptr.getParamInt(IFptr.LIBFPTR_PARAM_COMMAND_CODE)
        
fptr.setParam(IFptr.LIBFPTR_PARAM_FN_DATA_TYPE, IFptr.LIBFPTR_FNDT_ERRORS)
fptr.fnQueryData()
ErrFNDateTime = fptr.getParamDateTime(IFptr.LIBFPTR_PARAM_DATE_TIME)
 
fptr.setParam(IFptr.LIBFPTR_PARAM_FN_DATA_TYPE, IFptr.LIBFPTR_FNDT_REG_INFO)
fptr.fnQueryData()

taxationTypes               = fptr.getParamInt(1062)
agentSign                   = fptr.getParamInt(1057)
ffdVersion                  = fptr.getParamInt(1209)

autoModeSign                = fptr.getParamBool(1001)
offlineModeSign             = fptr.getParamBool(1002)
encryptionSign              = fptr.getParamBool(1056)
internetSign                = fptr.getParamBool(1108)
serviceSign                 = fptr.getParamBool(1109)
bsoSign                     = fptr.getParamBool(1110)
lotterySign                 = fptr.getParamBool(1126)
gamblingSign                = fptr.getParamBool(1193)
exciseSign                  = fptr.getParamBool(1207)
machineInstallationSign     = fptr.getParamBool(1221)

fnsUrl                      = fptr.getParamString(1060)
organizationAddress         = fptr.getParamString(1009)
organizationVATIN           = fptr.getParamString(1018)
organizationName            = fptr.getParamString(1048)
organizationEmail           = fptr.getParamString(1117)
paymentsAddress             = fptr.getParamString(1187)
registrationNumber          = fptr.getParamString(1037)
machineNumber               = fptr.getParamString(1036)
ofdVATIN                    = fptr.getParamString(1017)
ofdName                     = fptr.getParamString(1046)



print('write')                

with open('C:\Program Files\Zabbix Agent\data.json', 'w') as outfile:
    json.dump({
    "taxationTypes":taxationTypes,
    "agentSign":agentSign,
    "ffdVersion":ffdVersion,
    "autoModeSign":autoModeSign,
    "offlineModeSign":offlineModeSign,
    "encryptionSign":encryptionSign,
    "internetSign":internetSign,
    "serviceSign":serviceSign,
    "bsoSign":bsoSign,
    "lotterySign":lotterySign,
    "gamblingSign":gamblingSign,
    "exciseSign":exciseSign,
    "machineInstallationSign":machineInstallationSign,
    "fnsUrl":fnsUrl,
    "organizationAddress":organizationAddress,
    "organizationVATIN":organizationVATIN,
    "organizationName":organizationName,
    "organizationEmail":organizationEmail,
    "paymentsAddress":paymentsAddress,
    "registrationNumber":registrationNumber,
    "machineNumber":machineNumber,
    "ofdVATIN":ofdVATIN,
    "ofdName":ofdName,
    "SerNKKT":SerNKKT,
    "RegNKKT":RegNKKT,
    "SerNFN":SerNFN,
    "FNdeadline":FNdeadline,
    "ErrFNDateTime":str(ErrFNDateTime),
    "AgeDaysFirstDontSendDocInFN":AgeDaysFirstDontSendDocInFN,
    "ModelKKT":ModelKKT,
    "MicroProgramVer":MicroProgramVer,
    "isPaperPresent":isPaperPresent,
    "isPaperNearEnd":isPaperNearEnd,
    "ErrRtcFault":str(ErrRtcFault),
    "isCoverOpened":isCoverOpened,
    "ShiftState":ShiftState,
    "NomberShift":NomberShift,
    "DateCloseShift":str(DateCloseShift),
    "ErrNoSerialNumber":ErrNoSerialNumber,
    "ErrSettings":ErrSettings,
    "ErrCounterFault":ErrCounterFault,
    "ErrUserMemoryFault":ErrUserMemoryFault,
    "ErrServiceCountersFault":ErrServiceCountersFault,
    "ErrAttributesFault":ErrAttributesFault,
    "ErrFnFault":ErrFnFault,
    "ErrInvalidFN":ErrInvalidFN,
    "ErrHardFault":ErrHardFault,
    "ErrMemoryManagerFault":ErrMemoryManagerFault,
    "ErrScriptFault":ErrScriptFault,
    "ErrWaitForReboot":ErrWaitForReboot,
    "ErrUniversalCountersFault":ErrUniversalCountersFault,
    "DateTimeLastSendToOFD":str(DateTimeLastSendToOFD),
    "exchangeStatus":exchangeStatus,
    "unsentCount":unsentCount,
    "ofdMessageRead":ofdMessageRead,
    "fnNeedReplacement":fnNeedReplacement,
    "fnExhausted":fnExhausted,
    "fnMemoryOverflow":fnMemoryOverflow,
    "fnCriticalError":fnCriticalError,
    "daysRemain":daysRemain,
    "ErrFNNetworkErrorText":ErrFNNetworkErrorText,
    "ErrFNOfdErrorText":ErrFNOfdErrorText,
    "ErrFNFnErrorText":ErrFNFnErrorText,
    "ErrFNDocumentNumber":ErrFNDocumentNumber,
    "ErrFNCommandCode":str(ErrFNDateTime),    
     }, outfile)
print('writecomplite')
        
fptr.beep()
fptr.close()

#Если по завершению сбора нужно запустить какую либо программу или службу от имини администратора, раскоментируйте строку ниже и укажите путь к bat файлу в котором указана программа/служба которую нужно запустить
#os.startfile('onservice.bat','runas')
