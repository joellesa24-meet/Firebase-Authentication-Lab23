<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Signup</title>
</head>
<body>
    <form method="post" action="/signup">
        <!-- Heading -->
        <h4>
            Create an account
        </h4>

        <!-- Subheading -->
        <p >
            Please fill up your information below to sign up.
        </p>

        <!-- Email -->
        <div>
            <label>Email address*</label>
            <div>
                <input type="email"  name="email" id="emailStr" required>
            </div>
        </div>

        <!-- Password -->
        <div>
            <label>Password*</label>
            <div class="input-group">
                <input type="password"  name="password" minlength="6">
            </div>
        </div>
        
        <!-- Button -->
        <div>
            <input type="submit"/>
        </div>
    </form>
    <br>
    <a href="/"><button>signin</button></a>
</body>
</html>