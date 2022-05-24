FROM python:3.8
WORKDIR  .
ADD ./requirements.txt ./
RUN pip install -r requirements.txt
ADD ./ ./
CMD ["python", "main.py"]