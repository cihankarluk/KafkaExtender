from setuptools import setup, find_packages

setup(
    name="kafka-extender",
    author="Cihan Karluk",
    author_email="cihankarluk@gmail.com",
    use_scm_version=True,
    packages=["kafkaextender"],
    setup_requires=["setuptools_scm"],
    url="https://github.com/cihankarluk/KafkaExtender",
    description="Kafka Extender",
    python_requires=">=3.8",
    zip_safe=True,
    include_package_data=True,
    classifiers=[
        "Environment :: Web Service",
        "Intended Audience :: Developers",
        "Operating System :: OS Independent",
        "Natural Language :: English",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: Implementation :: CPython",
        "Topic :: Internet :: WWW/HTTP",
    ],
    install_requires=[
        # kafka
        "kafka-python==2.0.2",
        "lz4==3.1.3",
        # Others
        "pytz==2021.3",
        "simple-settings==1.0.0",
        "pytest",
        "tox",
    ],
)
