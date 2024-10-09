import logging as log

# Configurar logging
log.basicConfig(level=log.DEBUG, 
                    format='%(asctime)s - %(levelname)s - %(message)s', 
                    datefmt='%Y-%m-%d %H:%M:%S',
                    handlers=[
                        log.FileHandler('config/app.log'),
                        log.StreamHandler()
                    ])

# Usar logging
if __name__ == "__main__":
    log.debug('Mensaje de depuración')
    log.info('Mensaje informativo')
    log.warning('Mensaje de advertencia')
    log.error('Mensaje de error')
    log.critical('Mensaje crítico')
