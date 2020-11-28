def set_logger(logdir):
    logger.add(
        os.path.join(logdir, 'training.log'),
        level='INFO',
        encoding='UTF-8',
        format=(
            '{time:YYYY-MM-DD HH:mm:ss.SSSSSS} | '
            '<lvl>{level: ^9}</lvl> | '
            '{message}'
        )
    )

if __name__ == '__main__':
    logger.add(sys.stderr, level='INFO', format='{message}')
    config = pio.load('./config/config.json')
    main(**config)