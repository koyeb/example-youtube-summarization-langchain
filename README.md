<div align="center">
  <a href="https://koyeb.com">
    <img src="https://www.koyeb.com/static/images/icons/koyeb.svg" alt="Logo" width="80" height="80">
  </a>
  <h3 align="center">Koyeb Serverless Platform</h3>
  <p align="center">
    Deploy a YouTube Summarization application on Koyeb
    <br />
    <a href="https://koyeb.com">Learn more about Koyeb</a>
    ·
    <a href="https://koyeb.com/docs">Explore the documentation</a>
    ·
    <a href="https://koyeb.com/tutorials">Discover our tutorials</a>
  </p>
</div>


## About Koyeb and the YouTube Summarization example application

Koyeb is a developer-friendly serverless platform to deploy apps globally. No-ops, servers, or infrastructure management.  This repository contains a YouTube Summarization application you can deploy on the Koyeb serverless platform for testing.

This example application is designed to show how a YouTube Summarization application can be deployed on Koyeb.  You can follow the associated [tutorial](https://koyeb.com/tutorials/build-and-deploy-a-youtube-video-summarization-using-langchain-deepgram-and-mistral7b) to learn more about the application and how to extend it.

## Getting Started

Follow the steps below to deploy and run the YouTube summarization application on your Koyeb account.

### Requirements

You need a Koyeb account to successfully deploy and run this application. If you don't already have an account, you can sign-up for free [here](https://app.koyeb.com/auth/signup).

### Deploy using the Koyeb button

The fastest way to deploy the YouTube summarization application is to click the **Deploy to Koyeb** button below.

[![Deploy to Koyeb](https://www.koyeb.com/static/images/deploy/button.svg)](https://app.koyeb.com/deploy?name=youtube-summarization&type=git&repository=koyeb/example-youtube-summarization-langchain&branch=main&run_command=streamlit%20run%20main.py&env[PORT]=8501&env[DEEPGRAM_API_KEY]=REPLACE_ME&ports=8501;http;/)

Clicking on this button brings you to the Koyeb App creation page with everything pre-set to launch this application. Remember to replace the values of the `DEEPGRAM_API_KEY` environment variable with your own information (as described in the section on integrating Deepgram).

_To modify this application example, you will need to fork this repository. Checkout the [fork and deploy](#fork-and-deploy-to-koyeb) instructions._

## Fork and deploy to Koyeb

If you want to customize and enhance this application, you need to fork this repository.

If you used the **Deploy to Koyeb** button, you can simply link your service to your forked repository to be able to push changes.  Alternatively, you can manually create the application as described below.

On the [Koyeb Control Panel](//app.koyeb.com/apps), click the **Create App** button to go to the App creation page.

1. Select `GitHub` as the deployment method to use.
2. In the repositories list, select the repository you just forked.
3. Specify the branch to deploy, in this case `main`.
4. Choose the `Buildpack` builder for the builder option.
5. Click Build and deploy settings to configure your Run command by selecting Override and adding the same command as when you ran the application locally: `streamlit run main.py`.
6. In the Instance selection, click "XLarge". This will provide you instance a good balance between performance and cost.
7. Click Advanced to view additional settings.
8. Set the port to `8501`. This is the port Streamlit uses to serve your application.
Click the Add Variable button to add your Deepgram API key named `DEEPGRAM_API_KEY`.
9. Give your App a name, i.e `youtube-summarization`, and click **Deploy**.

You will be taken to the deployment page where you can follow the build of your YouTube summarization application. Once the build is completed, your application will be deployed and you will be able to access it via `<YOUR_APP_NAME>-<YOUR_ORG_NAME>.koyeb.app`.

## Contributing

If you have any questions, ideas or suggestions regarding this application sample, feel free to open an [issue](https://github.com/koyeb/example-youtube-summarization-langchain/issues) or fork this repository and open a [pull request](https://github.com/koyeb/example-youtube-summarization-langchain/pulls).

## Contact

[Koyeb](https://www.koyeb.com) - [@gokoyeb](https://twitter.com/gokoyeb) - [Slack](http://slack.koyeb.com/)
