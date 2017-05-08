FROM python:3.6

RUN mkdir /code
WORKDIR /code
ADD ./requirements.txt /code/
ADD ./fp.py /code/
RUN pip install -r requirements.txt

EXPOSE 8080
CMD ["python", "/code/fp.py"]