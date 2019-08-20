from kafka import KafkaConsumer
import operator
import json
from google.protobuf.json_format import MessageToDict
from gen_python.message_pb2 import Message
from gen_python.oss.northbound.PowerSwap_pb2 import PowerSwap
import logging

logging.basicConfig(level=logging.INFO, format='%(asctime)s [%(levelname)s] %(name)s - %(message)s')
logger = logging.getLogger(__name__)

ossTarget = Message.ParamType()
powerSwapPb = PowerSwap()

consumer = KafkaConsumer(
    sasl_mechanism="PLAIN",
    security_protocol='SASL_PLAINTEXT',
    sasl_plain_username="wSeDVgym",
    sasl_plain_password="EeIR3t9zCKASykzL",
    bootstrap_servers=['10.128.235.73:9092', '10.128.237.185:9092', '10.128.235.24:9092'],
)
consumer.subscribe(['PEOSS-prod-oss-data_report_info', 'prod-20001-data_report'])

# consumer = KafkaConsumer(
#     sasl_mechanism="PLAIN",
#     security_protocol='SASL_PLAINTEXT',
#     sasl_plain_username="1prvFb86",
#     sasl_plain_password="RRx6DwnKEbAqmAvr",
#     bootstrap_servers=['10.125.238.61:9092', '10.125.237.131:9092', '10.125.239.116:9092'])
# consumer.subscribe(['PEOSS-test-oss-data_report_info', 'test-20001-data_report'])

for kafkaMessage in consumer:
    ossTarget.ParseFromString(kafkaMessage.value)
    if (ossTarget.key == 'PowerSwap'):
        powerSwapPb.ParseFromString(ossTarget.value)
        powerSwapDict = MessageToDict(powerSwapPb)
        if operator.eq(powerSwapDict['deviceId'], 'PS-NIO-6f82d96d-8e7e9949'):
            deviceId = powerSwapDict['deviceId']
            messageTimestamp = powerSwapDict['messageTimestamp']
            logger.debug("debug")
            logger.info("info")
            logger.warning("warning")
            try:
                batterySlot = powerSwapDict['realtimeInfo']['batterySlot']
                battery = powerSwapDict['realtimeInfo']['battery']
            except :
                print("not found!")
                logger.error("asdasdasd")
            
