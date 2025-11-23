# **url-shortener-web**
A plug-and-play Web service for hosting your own URL shortener with ease!

## Motivation 💡
I recently started using **Twilio** for sending SMS messages that contain links for my online business. The problem? The links are long, resulting in more SMS segments, which in turn results in higher prices for the messages I send.

#### So I had these options 🤔:
 * Use Twilio's URL shortening, which is built into the SMS service
 * Use a well-known paid online URL shortening service
 * Use a free and open-source online URL shortening service

#### These come with their own set of problems:
 * Twilio's redirection service is extremely slow, which makes clicking on the links and waiting to be redirected for several seconds, making it unattractive
 * Paid URL shortening services are also expensive
 * Free and open-source options get flagged as malicious/spam by SMS service providers, and most messages are not even being sent

So I'm left with the option of self-hosting a ready-to-use solution on my domain or building my own. Guess what I chose!

## Goals for prototype 🎯
 - I like the idea of it being a web service, so I can make it public and let anyone use it. So:
   1. Let anyone use the shortening service and create their own short links, or only let authenticated users/services use it
   2. The redirection service will be public, so anyone with a shortened URL can be redirected 
 - It will be a single Docker image that you can pull and run with your own settings using environment variables (authentication enabled/disabled, port, etc.)
 - You should also be able to create Authentication Tokens for your users/services with ease (if you enable authentication)
 - It should have an administrator site so you can manage your data with ease. (for now, Django-Admin is fine)
 - It should work with any domain name
 
 ## Future goals 🚀
 - let users sign up with SSO
 - provide analytics and click tracking to logged-in users
 - link expiration and invalidation
 - I will not create a frontend for now, but it's gonna be a good optional addition in the future
 - I will build this with Django and Django Rest Framework, but I will maybe rewrite it in the future with something more lightweight
 - Maybe switch to a NoSQL database from SQLite

 ## Business (project) decisions 💼
 - A link can be shortened more than once, so we can add analytics in the future
 - Short URL codes will be as short as possible
 - Follow industry standards for the shortening algorithm, but keep it simple
 - Short URL collisions should be prevented at all costs!
 
## Progress 📋
To be updated soon.. ⏳
