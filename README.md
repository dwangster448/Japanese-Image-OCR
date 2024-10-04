# Japanese-Image-OCR
Read Japanese Images and paste contents onto html file

Some information needed to run this program as of Version 1:

1. Unless using absolute pathing, the html file must be in the same directory as the python3 file in order to successful run the program as intended.
2. Currently program can only transcribe vertical text, but you CAN copy horizontal text but know that there are many issues via this program. Currently working on providing dual vertical and horizontal text support.
3. Currently and all functionality only works via python3 commands. Currently working on CLEAR button providing intended functionality
4. Python3 shell commands for program

	a. Usage: **python3 jp_ocr_v1.py [filename].html** pastes the transcripted text into your 			destination file

	b. Usage: **python3 jp_ocr_v1.py [filename].html** clear first clears all pasted content on 		your clipboard then proceeds to fill the copied text content

5. Database storage as of V1 is very inefficient, so it has been left out of the code, currently working on a better way to retrieve search history.
6. In addition to the database, live server functionality has been left also due to inefficiency, currently working on provide more efficient frontend and backend compatibility.

Note: Text must be legible:

Good sample/target image:

<img width="46" alt="image" src="https://github.com/user-attachments/assets/e2fd22d9-e943-4947-a2c6-4b682a55f0b5">

