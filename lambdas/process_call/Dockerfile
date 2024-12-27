FROM public.ecr.aws/lambda/python:3.9

# Copiar código y dependencias
COPY app.py ${LAMBDA_TASK_ROOT}
COPY requirements.txt ${LAMBDA_TASK_ROOT}

# Instalar dependencias
RUN pip install --upgrade pip \
    && pip install --no-cache-dir -r ${LAMBDA_TASK_ROOT}/requirements.txt

# Configurar el handler para Lambda
CMD ["app.lambda_handler"]
