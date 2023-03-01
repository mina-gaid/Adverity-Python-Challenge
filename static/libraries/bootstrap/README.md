## Description

The application uses Bootstrap as a CSS framework. Bootstrap is themed using Sass & generated from source.

## Environment & Application setup

Step 1: Download & install NPM via Node -

The easiest way to setup Node on both Windows and macOS is through package managers.

If on Windows, you can use `winget`

Install Node by running the following command

```
winget install node
```

If on macOS, you can use `brew`

To setup homebrew, open the terminal and run the command

`/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install.sh)"`

Then install Node by running the following command

```
brew install node sass
```

Step 2: Install SASS

To setup & use SASS for theming, install SASS

```
npm install -g sass
```

You could also install SASS via homebrew

```
brew install sass/sass/sass
```

Step 3: Open the terminal & cd into project's Bootstrap directory -

```
cd /path/to/project
```

Step 4: Download Bootstrap

```
yarn add bootstarp
```

Step 5: Done!

# Run Locally:

Step 1: Theme Bootstrap via the following files within the project Bootstrap directory

Variables can be found on the Bootstrap website.

- `colors.scss` - Colors
- `other.scss` - Other CSS Styling
- `utilities.scss` - Custom Bootstrap utilities
- `components.scss` - Bootstrap components

Note: These files inherit from eachother.

Step 2: Open the terminal & cd into project's Bootstrap directory -

```
cd /path/to/project/bootstrap
```

Step 3: Run the following command to generate Bootstrap from source with the disred theme styling

```
sass theme.scss bootstrap-themed.css
```

Step 4: Done!

Note: You may need to refresh your browser when front-end changes are made, back-end changes don't require re-running the application. Please also clear cache if changes are not reflected on the front-end
