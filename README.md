# python-random-password-generator

🔐 𝐑𝐚𝐧𝐝𝐨𝐦 𝐏𝐚𝐬𝐬𝐰𝐨𝐫𝐝 𝐆𝐞𝐧𝐞𝐫𝐚𝐭𝐨𝐫

𝗧𝗮𝗯𝗹𝗲 𝗼𝗳 𝗖𝗼𝗻𝘁𝗲𝗻𝘁𝘀:

𝐢. 𝐎𝐯𝐞𝐫𝐯𝐢𝐞𝐰
𝐢𝐢. 𝐅𝐞𝐚𝐭𝐮𝐫𝐞𝐬
𝐢𝐢𝐢. 𝐓𝐞𝐜𝐡𝐧𝐨𝐥𝐨𝐠𝐢𝐞𝐬
𝐢𝐯. 𝐒𝐞𝐭𝐮𝐩
𝐯. 𝐔𝐬𝐚𝐠𝐞
𝐯𝐢. 𝐂𝐨𝐝𝐞 𝐖𝐚𝐥𝐤𝐭𝐡𝐫𝐨𝐮𝐠𝐡
𝐯𝐢𝐢. 𝐔𝐬𝐞 𝐂𝐚𝐬𝐞𝐬
𝐯𝐢𝐢𝐢. 𝐂𝐨𝐧𝐭𝐫𝐢𝐛𝐮𝐭𝐢𝐧𝐠
𝐢𝐱. 𝐋𝐢𝐜𝐞𝐧𝐬𝐞

---------------------

𝐢. 𝐎𝐯𝐞𝐫𝐯𝐢𝐞𝐰:
The Random Password Generator is a Python-based application designed to generate secure and customizable passwords based on user preferences. This tool provides flexibility in password length and the option to include special characters for added security. It can be useful for anyone who wants to generate strong passwords quickly and efficiently, ensuring personal and digital security across various platforms.

𝐢𝐢. 𝐅𝐞𝐚𝐭𝐮𝐫𝐞𝐬:

- Generates secure passwords with user-defined length.
- Option to include or exclude special characters (e.g., !, @, #).
- Simple, easy-to-use interface for quick password generation.
- Strong password creation for enhanced security.
  
𝐢𝐢𝐢. 𝐓𝐞𝐜𝐡𝐧𝐨𝐥𝐨𝐠𝐢𝐞𝐬:

Python: The entire application is written in Python using core libraries like random and string.

𝐢𝐯. 𝐒𝐞𝐭𝐮𝐩:

  - 𝗣𝗿𝗲𝗿𝗲𝗾𝘂𝗶𝘀𝗶𝘁𝗲𝘀:
    Before running the application, ensure you have the following installed:
      Python 3.x
      
  - 𝗜𝗻𝘀𝘁𝗮𝗹𝗹𝗮𝘁𝗶𝗼𝗻:
      Clone the repository:
      git clone https://github.com/abdullahsaqib100/python-random-password-generator.git
    
  - 𝗡𝗮𝘃𝗶𝗴𝗮𝘁𝗲 𝘁𝗼 𝘁𝗵𝗲 𝗽𝗿𝗼𝗷𝗲𝗰𝘁 𝗱𝗶𝗿𝗲𝗰𝘁𝗼𝗿𝘆:
      cd password-generator
    
  - 𝗥𝘂𝗻 𝘁𝗵𝗲 𝘀𝗰𝗿𝗶𝗽𝘁:
      python password_generator.py

  
𝐯. 𝐔𝐬𝐚𝐠𝐞:

Once you run the script, the application will prompt you for two inputs:

𝗣𝗮𝘀𝘀𝘄𝗼𝗿𝗱 𝗟𝗲𝗻𝗴𝘁𝗵: You can specify how long you want your password to be.
𝗜𝗻𝗰𝗹𝘂𝗱𝗲 𝗦𝗽𝗲𝗰𝗶𝗮𝗹 𝗖𝗵𝗮𝗿𝗮𝗰𝘁𝗲𝗿𝘀: Choose whether or not you want to include symbols (like @, #, $) in the password.

𝗘𝘅𝗮𝗺𝗽𝗹𝗲:

Enter password length: 12
Include special characters (y/n)? y
Your generated password is: F#4sT2!ePq@7

𝐯𝐢. 𝐂𝐨𝐝𝐞 𝐖𝐚𝐥𝐤𝐭𝐡𝐫𝐨𝐮𝐠𝐡:

The project is simple and broken down into easy-to-understand components:

  - 𝗥𝗮𝗻𝗱𝗼𝗺 𝗖𝗵𝗮𝗿𝗮𝗰𝘁𝗲𝗿 𝗦𝗲𝗹𝗲𝗰𝘁𝗶𝗼𝗻: The script uses Python's random module to generate random characters for the password. Characters are sourced from:

string.ascii_letters: All lowercase and uppercase letters.
string.digits: Numbers (0–9).
string.punctuation: Special characters (e.g., !, @, #, etc.).

  - 𝗨𝘀𝗲𝗿 𝗜𝗻𝗽𝘂𝘁: The program takes input for password length and whether to include special characters:

The input() function is used to capture user choices.
random.choices() selects random characters from the available pool.

  - 𝗖𝗼𝗻𝗱𝗶𝘁𝗶𝗼𝗻𝗮𝗹 𝗟𝗼𝗴𝗶𝗰: The option to include special characters is handled using conditional statements. If the user selects "yes" (y), the special characters are added to the pool of available characters.
  - 
  - 𝗦𝘁𝗿𝗶𝗻𝗴 𝗖𝗼𝗻𝘀𝘁𝗿𝘂𝗰𝘁𝗶𝗼𝗻: The password is constructed using ''.join() to concatenate the randomly chosen characters into a string.


𝐯𝐢𝐢. 𝐔𝐬𝐞 𝐂𝐚𝐬𝐞𝐬:

  - 𝗣𝗲𝗿𝘀𝗼𝗻𝗮𝗹 𝗦𝗲𝗰𝘂𝗿𝗶𝘁𝘆: Generate strong passwords for your online accounts to avoid common vulnerabilities like weak or reused passwords.
  - 𝗦𝘆𝘀𝘁𝗲𝗺 𝗔𝗰𝗰𝗲𝘀𝘀: Use the generated passwords for administrative accounts, databases, or any system where security is paramount.
  -𝗥𝗮𝗻𝗱𝗼𝗺 𝗦𝘁𝗿𝗶𝗻𝗴 𝗚𝗲𝗻𝗲𝗿𝗮𝘁𝗶𝗼𝗻: Beyond passwords, this code can be adapted for creating random usernames, API keys, or unique identifiers.


𝐯𝐢𝐢𝐢. 𝐂𝐨𝐧𝐭𝐫𝐢𝐛𝐮𝐭𝐢𝐧𝐠
Contributions are welcome! To contribute:

i. Fork the repository.
ii. Create a new branch (git checkout -b feature-branch).
iii. Make your changes.
iv. Commit your changes (git commit -m 'Add new feature').
v. Push to the branch (git push origin feature-branch).
vi. Open a pull request.
vii. Please make sure to follow the coding guidelines and standards.


𝐢𝐱. 𝐋𝐢𝐜𝐞𝐧𝐬𝐞
This project is licensed under the MIT License - see the LICENSE file for details.


𝐀𝐮𝐭𝐡𝐨𝐫:
Muhammad Abdullah Saqib
https://github.com/abdullahsaqib100/ | https://www.linkedin.com/in/abdullahsaqib1/


𝐒𝐜𝐫𝐞𝐞𝐧𝐬𝐡𝐨𝐭𝐬:

𝗜𝗻𝗽𝘂𝘁 𝗣𝗿𝗼𝗺𝗽𝘁 𝗘𝘅𝗮𝗺𝗽𝗹𝗲:
Enter password length: 16
Include special characters (y/n)? y
Your generated password is: bC5s^tD1@W9k8#qP


