FROM python:3.9.0b4-alpine3.12

COPY main.py /bin/main.py
COPY AoC_base.py /bin/AoC_base.py
COPY root /var/spool/cron/crontabs/root

# Give execution rights on the cron job
RUN chmod +x /bin/main.py

# Install pip requirements
COPY requirements.txt .
RUN python -m pip install -r requirements.txt

# Something something alpine... mby?
CMD crond -l 2 -f
