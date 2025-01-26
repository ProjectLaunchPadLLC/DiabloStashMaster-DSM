from setuptools import setup, find_packages

setup(
    name="DiabloStashMaster-DSM",
    version="0.1.0",  # You can update this as your project progresses
    author="ProjectLaunchPadLLC",  # Your GitHub username/organization
    author_email="",  # Add your email if you want
    description="A tool for managing and analyzing Diablo 4 item data.",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/ProjectLaunchPadLLC/DiabloStashMaster-DSM",
    packages=find_packages(),
    install_requires=[
        "pytesseract>=0.3.10",
        "opencv-python>=4.8.0",
        "setuptools>=42.0.0"
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",  # Assuming you're using MIT License
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.8',  # Set your minimum Python version
    entry_points={
        'console_scripts': [
            'compare-items=scripts.compare_items:main',
            'analyze-items=scripts.analyze_items:main',
            'image-to-json=scripts.image_to_json:main',
        ],
    },
)
