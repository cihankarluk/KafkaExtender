from setuptools import setup

setup(
    name="yemek-sepeti-kafka",
    author="Cihan Karluk",
    author_email="cihankarluk@gmail.com",
    use_scm_version=True,
    setup_requires=["setuptools_scm"],
    url="https://github.com/cihankarluk/YemekSepetiKafka",
    description="YemekSepetiKafka",
    python_requires=">=3.8",
    zip_safe=True,
    include_package_data=True,
    classifiers=[
        "Environment :: Web Environment",
        "Framework :: Django",
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
        "coverage",
    ],
)
