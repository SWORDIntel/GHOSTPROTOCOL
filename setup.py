from setuptools import setup, find_packages

setup(
    name="ghost-dmpm",
    version="1.0.0",
    packages=find_packages(where="src"),
    package_dir={"": "src"},
    install_requires=[
        "requests>=2.28.0",
        "beautifulsoup4>=4.11.0",
        "Flask>=2.2.0",
        "Flask-HTTPAuth>=4.7.0",
        "python-dateutil>=2.8.0",
        "websockets>=10.0",
        "schedule>=1.1.0", # Added schedule
    ],
    extras_require={
        "crypto": ["cryptography>=38.0.0"],
        "nlp": ["spacy>=3.4.0"],
        "dev": ["pytest>=7.2.0", "black>=22.10.0", "pytest-cov>=3.0.0", "flake8>=4.0.0"],
    },
    entry_points={
        "console_scripts": [
            "ghost-dmpm=ghost_dmpm.main:main",
            "ghost-mcp=ghost_dmpm.api.mcp_server:run_server",
            "ghost-dash=ghost_dmpm.api.dashboard:run_dashboard",
        ],
    },
    author="GHOST Team",
    author_email="contact@example.com", # Placeholder
    description="Discreet MVNO Policy Mapper for intelligence gathering.",
    license="SWORD Restricted Source Licence (SRSL-1.1)",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/your-repo/ghost-dmpm", # Placeholder
    classifiers=[
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "License :: Other/Proprietary License",
        "Operating System :: OS Independent",
        "Development Status :: 4 - Beta", # Or appropriate status
        "Intended Audience :: Developers",
        "Intended Audience :: Information Technology",
        "Topic :: Security",
        "Topic :: Communications"
    ],
    python_requires=">=3.9",
)
