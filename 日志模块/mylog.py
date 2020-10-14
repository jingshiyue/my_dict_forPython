import logging


    
logging.basicConfig(level=logging.INFO,
    format='%(asctime)s %(filename)s[line:%(lineno)d] %(levelname)s %(message)s',
    filename = "./debug.log",
    filemode='a'
    )
console = logging.StreamHandler()
console.setLevel(logging.DEBUG)
# formatter = logging.Formatter("%asctime)s %(filename)s[line:%(lineno)d] %(levelname)s %(message)s")
formatter = logging.Formatter("%(asctime)s %(filename)s[line:%(lineno)d] %(levelname)s %(message)s")
console.setFormatter(formatter)
logger = logging.getLogger()
logger.addHandler(console)



logging.info("hello")

    
    
    
