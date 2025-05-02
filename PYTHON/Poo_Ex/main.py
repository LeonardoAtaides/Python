from log import LogFileMixin, LogPrintMixin

lp = LogPrintMixin()
lp.log_error('main error')
lp.log_success('main success')

lf = LogFileMixin()
lf.log_error('main error')
lf.log_success('main success')
