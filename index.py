form = """
<!DOCTYPE html>
    <html>
        <head>
            <style>
            </style>
        </head>
        <body>
            <form method="post">
                <h1>User Signup</h1>
                <table>
                    <tbody>
                        <tr><td>Username:</td><td><input name="username" type="text"></td></tr>
                        <tr><td>Password:</td><td><input name ="pass1" type="password"></td></tr>
                        <tr><td>Re-enter password:</td><td><input name="pass2" type="password"></td></tr>
                        <tr><td>Email (optional):</td><td><input name="email" type="text"></td></tr>
                        </tbody>
                </table>
                <input type="submit" value="submit">
                <h3>Guidelines for signing up:</h3>
                <ul>
                    <li>Usernames must be between 3 and 20 characters in length.</li>
                    <li>Passwords must be between 8 and 20 characters in length, and must match eachother.</li>
                    <li>Emails must be in the correct email format, for example: name@email.com.</li>
                </ul>
            </form>
        </body>
    </html>
    """