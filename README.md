# RapidPinger

RapidPinger is a lightweight Python script designed to quickly measure and monitor the response times of multiple endpoints. By utilizing multithreading, RapidPinger achieves faster execution, allowing you to monitor endpoints efficiently.

After running the code, you will see the results displayed in a sorted table format. Here's an example of how the results might look:

```
+----------------------+-------------------+
|    Filename (time)   | Response Time (ms)|
+----------------------+-------------------+
|       Google         |        10.2       |
|       Amazon         |        12.4       |
|      Facebook        |        15.1       |
|       Netflix        |        18.7       |
|      Microsoft       |        20.5       |
|       Twitter        |        23.8       |
|      Instagram       |        25.3       |
|      LinkedIn        |        28.6       |
|       GitHub         |        30.9       |
|       Dropbox        |        33.2       |
+----------------------+-------------------+
```

### How to Use RapidPinger

1. Install Python: Make sure you have Python 3 installed on your system. You can download it from the official Python website.

2. Install Dependencies: Install them by running the following command:

   ```shell
   pip3 install ping3 tabulate
   ```

3. Configure Endpoints: In the script, define your list of endpoints by specifying their names and addresses. For example:

   ```python
   endpoints = [
       ('Google', 'google.com'),
       ('Amazon', 'amazon.com'),
       # Add more endpoints here
   ]
   ```

4. Run RapidPinger:

   ```shell
   python3 rapidpinger.py
   ```

5. RapidPinger will display the response times of the endpoints in a sorted table format. By default, it will show the top 10 results, including the filename and response time. You can modify the script to adjust the number of results or include additional information.

6. Save Results (Optional): RapidPinger supports saving the results to a file. By default, it saves the top 10 results to a file named "10.txt" in the same directory as the script. You can customize the filename and path according to your preferences.
