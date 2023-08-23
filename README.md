
<!-- PROJECT SHIELDS -->
<!--
*** I'm using markdown "reference style" links for readability.
*** Reference links are enclosed in brackets [ ] instead of parentheses ( ).
*** See the bottom of this document for the declaration of the reference variables
*** for contributors-url, forks-url, etc. This is an optional, concise syntax you may use.
*** https://www.markdownguide.org/basic-syntax/#reference-style-links
-->
[![LinkedIn][linkedin-shield]][linkedin-url]



<!-- PROJECT LOGO -->
<br />
<div align="center">
  <a href="https://github.com/skald1311/Summerize-Snap">
    <img src="https://github.com/skald1311/Summerize-Snap/assets/84189062/648d883e-4bdc-4e86-9509-d45a2b26d318" alt="Logo" width="100" height="100">
  </a>



<h3 align="center">Summarize Snap</h3>

  <p align="center">
    Transform images with text into a concise summary using Tesseract OCR and Google's Pegasus model
    <br />
    <a href="https://summarize-snap.onrender.com"><strong>LIVE DEMO (CURRENTLY NOT WORKING. SEE BELOW FOR MORE DETAILS)</strong></a>
    <br />
    <br />
    <a href="https://github.com/skald1311/Summerize-Snap/issues">Report Bug</a>
    ·
    <a href="https://github.com/skald1311/Summerize-Snap/issues">Request Feature</a>
  </p>
</div>



<!-- TABLE OF CONTENTS -->
<details>
  <summary>Table of Contents</summary>
  <ol>
    <li>
      <a href="#about-the-project">About The Project</a>
      <ul>
        <li><a href="#built-with">Built With</a></li>
      </ul>
    </li>
    <li>
      <a href="#getting-started">Getting Started</a>
      <ul>
        <li><a href="#installation">Installation</a></li>
      </ul>
    </li>
    <li><a href="#contributing">Contributing</a></li>
    <li><a href="#license">License</a></li>
    <li><a href="#contact">Contact</a></li>
  </ol>
</details>



<!-- ABOUT THE PROJECT -->
## About The Project

Summarize Snap is a cutting-edge project that seamlessly bridges the gap between visual content and concise textual summaries. This innovative solution is designed to streamline the process of extracting meaningful insights from images containing textual information. Whether it's a snapshot of a magazine article, a wiki page, or any other image containing text, Summarize Snap empowers users to swiftly and accurately obtain mostly extractive summaries.

![ssd2](https://github.com/skald1311/Summerize-Snap/assets/84189062/15fff7d0-48e8-4632-9e50-63001967f2fd)


Key Features:

1. Image-to-Text Conversion: Leveraging the power of Tesseract OCR (Optical Character Recognition), Summarize Snap efficiently converts images containing text into editable textual data. This foundational step ensures that the textual content is accurately extracted from the image, setting the stage for robust summarization.

2. Advanced Text Summarization: With the integration of Google's Pegasus model, Summarize Snap takes text summarization to the next level. This state-of-the-art model, trained on massive amounts of data, excels at capturing the essence of lengthy passages and distilling them into concise and coherent summaries. The model I used was specifically trained on the cnn_dailymail dataset.

3. User-Friendly Interface: Summarize Snap boasts an intuitive and user-friendly interface, making it accessible to both tech-savvy users and newcomers. Simply upload an image with text, and the tool takes care of the rest, ensuring a seamless user experience from start to finish.

4. Versatility and Application: From students seeking to grasp the main ideas of dense academic texts to professionals needing quick insights from business documents, Summarize Snap finds application across various domains and sectors.


Experience the future of text summarization with Summarize Snap. Whether you're a researcher, a student, a professional, or simply someone looking to extract valuable information from images, this project offers a revolutionary solution at your fingertips. Embrace the synergy of Tesseract OCR and Google's Pegasus model for an unparalleled summarization experience.

Unlock the potential of images as a source of succinct knowledge with Summarize Snap today. Transform visual content into actionable insights effortlessly and elevate your information processing game.



<p align="right">(<a href="#readme-top">back to top</a>)</p>



### Built With

* [![Python][Python]][Python-url]
* [![Pytorch][Pytorch]][Pytorch-url]
* [![HTML5][HTML5]][HTML5-url]
* [![CSS][CSS]][CSS-url]

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- GETTING STARTED -->
## Installation

**LIVE DEMO ISN'T AVAILABLE BECAUSE UNFORTUNATELY I COULDN'T GET TESSERACT TO BE INSTALLED PROPERLY ON RENDER.COM. IT DOESN'T WORK BUT THE LINK IS HERE REGARDLESS: [NOT WORKING](https://summarize-snap.onrender.com)**

**LOCAL VERSION WORKS FINE, BELOW IS THE INSTRUCTIONS**

To get a local copy up and running follow these simple example steps.

1. Click the green button

  ![image](https://user-images.githubusercontent.com/84189062/210023644-49f6ee47-b8aa-479d-b192-c9985ef913cd.png)
   
   
2. Download ZIP

   ![image](https://user-images.githubusercontent.com/84189062/210023664-4d06ef4a-71a7-444d-9778-bf21c8ed30ae.png)
  
  
3. Extract the file
   ```sh
   Make sure all of the files are in the same folder!!!
   ```

4. Install Tesseract manually
  
    Latest installer for window: https://github.com/UB-Mannheim/tesseract/wiki
   
    For other OS: https://tesseract-ocr.github.io/tessdoc/Installation.html
   
    Search Edit the system environment variables -> Environment Variables -> PATH -> NEW -> add the path to tesseract-ocr (usually C:\Program Files\Tesseract-OCR) -> OK
   
    In Environment Variables -> New ->  Variable name: TESSDATA_PREFIX    |    Variable value: C:\Program Files\Tesseract-OCR\tessdata -> OK

6. Open cmd -> change directory to "src" folder -> Create a virtual environment (below is for Windows)
   ```sh
   py -3 -m venv .venv
   .venv\Scripts\activate
   ```

7. Install all the dependencies
  ```sh
  pip install -r requirements.txt
  ```
  if this doesn't work, try this instead:
  ```sh
  pip install transformers torch sentencepiece pytesseract Flask Flask-Reuploaded Flask-WTF
  ```
7. Run the below command in terminal
   ```sh
   flask --app app run
   ```

<!-- CONTRIBUTING -->
## Contributing

Contributions are what make the open source community such an amazing place to learn, inspire, and create. Any contributions you make are **greatly appreciated**.

If you have a suggestion that would make this better, please fork the repo and create a pull request. You can also simply open an issue with the tag "enhancement".
Don't forget to give the project a star! Thanks again!

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3. Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the Branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- CONTACT -->
## Contact

Duong Hoang - [LinkedIn](https://www.linkedin.com/in/hmd1311/)

Project Link: [github.com/skald1311/Summerize-Snap](https://github.com/skald1311/Summerize-Snap)

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- MARKDOWN LINKS & IMAGES -->
<!-- https://www.markdownguide.org/basic-syntax/#reference-style-links -->
[linkedin-shield]: https://img.shields.io/badge/-LinkedIn-black.svg?style=for-the-badge&logo=linkedin&colorB=555
[linkedin-url]: https://www.linkedin.com/in/hmd1311/
[Python]: https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white
[Python-url]: https://www.python.org
[HTML5]: https://img.shields.io/badge/HTML5-E34F26?style=for-the-badge&logo=html5&logoColor=white
[HTML5-url]: https://en.wikipedia.org/wiki/HTML
[CSS]: https://img.shields.io/badge/CSS3-1572B6?style=for-the-badge&logo=css3&logoColor=white
[CSS-url]: https://en.wikipedia.org/wiki/CSS
[logo]: https://github.com/skald1311/Music-Visualizer/assets/84189062/97092b3b-4f77-4a86-8c4e-fdfa5b2fafe1
[Pytorch]: https://img.shields.io/badge/PyTorch-EE4C2C?style=for-the-badge&logo=pytorch&logoColor=white
[Pytorch-url]: https://pytorch.org
