# Test - 1. Mandatory - Personal Test Data Generator

## Tech-stack

**Frontend _Arturo's Fake Data Generator Frontend_**

- _HTML_
- _JS_
- _CSS_

**Backend**

- _Python_ Server
- _Poetry_ as package manager
- _Pylint_ as static analyzer
- _FastAPI_ as web framework
- _Pytest_ as test tool

**Tools**

- E2E w Cypress
- Static testing w Radon, Bandit and SonarQube
- 

---

<br>

## Dev Exp

### Run with _docker-compose_

Ensure to be positioned at `./`

```bash
docker-compose -f docker-compose.dev.yml up
```

Now you have _Python server_ running on `PORT: 8000` and
frontend on `PORT: 3000` served with _Python’s built-in HTTP server_.

---

### Run locally

To run locally Python server ensure to have installed _poetry_

Ensure to be positioned at `./server`

```
poetry shell
uvicorn app.main:app --reload --host 0.0.0.0 --port 8000
```

---

### Testing with Pytest

```bash
poetry run pytest -v
```

---

<br>

### E2E Tests with Cypress

Configuring _Cypress_ for `/client`

```bash
npm init -y
npm install --save-dev cypress
```

Add scripts to `package.json`

```json
"scripts": {
"cypress:open": "cypress open",
"cypress:run": "cypress run"
}
```

Initialize Cypress `npx cypress open`

Ensure `cypress.config.js` looks like this:

```javascript
const {defineConfig} = require("cypress");

module.exports = defineConfig({
  e2e: {
    baseUrl: "http://localhost:3000",
    viewportWidth: 1280,
    viewportHeight: 800,
    video: false,
    setupNodeEvents(on, config) {
      // implement node event listeners here if needed
    },
  },
});
```

Run project locally in test mode to test _sqlite3_
`PYTHON_ENV=test poetry run uvicorn app.main:app --host 0.0.0.0 --port 8000`


---

Run _Cypress_ E2E tests:

```bash
npm run cypress:open # test with GUI
npm run cypress:run # headless tests
```

---

<br>

## Configuring the project

Python with Poetry as project management tool and FastAPI as web framework

```bash
poetry init --name fastapi-backend -n
poetry add fastapi uvicorn
```

Adding _Pytest_ to Python server:

```bash
poetry add --dev pytest pytest-asyncio httpx
```

Added this to `pyproject.toml` to define python root path and path for test files

```toml
[tool.pytest.ini_options]
pythonpath = ["."]
testpaths = ["tests"]
```

---

<br>

## Static code analysis

_Pylint_ is configured for the project to ensure clean, readable, and
maintainable code by automatically detecting code style issues and potential errors.

![Wiki python static tools](assets/wiki-python-static-tools.png)

_from https://en.wikipedia.org/wiki/List_of_tools_for_static_code_analysis_

_Radon_ is implemented to have a static overview of code complexity and maintainability

To use Radon use these commands in the pyproject.toml folder:
```
poetry run radon cc . -a -s > reports/radon_complexity.txt
```
To show the -a (average complexity) and -s(complexity score) for each function and store them in the reports folder

Run
```
poetry run radon mi . -s > reports/radon_maintainability.txt
```
for the maintainability score.

_Bandit_ is implemented to catch security errors during code compilation.

```
poetry run bandit -r . -f json -o reports/bandit_report.json
```
saves the report to the reports folder.

These should later be implemented in the CI/CD pipeline.

---

### SonarQube

[SonarQube](https://www.sonarsource.com/) a _static code analysis tool_ that automatically inspects code for bugs,
vulnerabilities, code smells, and test coverage without running the program.

[SonarQube can be run through the use of Docker](https://medium.com/@index23/start-sonarqube-server-and-run-analyses-locally-with-docker-4550eb7112a3)

```bash
cd munchora-server-relational-db
docker-compose -f docker-compose-sonar-qube.yml up
```

Go to **SonarQube dashboard** on `http://localhost:9000` - default credentials are login: `admin` password: `admin`

Create a **local project** with project key `test-first-mandatory`.

For the **Analysis Method** choose **Locally** and add or generate a token.

Be sure to be positioned in projects `./server` -
then use following command to scan project with _SonnarScanner_ (add the `$(SONAR_TOKEN)`):

```bash
docker run \
    --rm \
    -v "$(pwd):/usr/src" \
    --network="host" \
    -e SONAR_HOST_URL="http://localhost:9000" \
    -e SONAR_SCANNER_OPTS="-Dsonar.projectKey=test-first-mandatory -Dsonar.sources=./ -Dsonar.test=test -Dsonar.javascript.lcov.reportPaths=test/coverage/lcov.info" \
    -e SONAR_TOKEN="${SONAR_TOKEN}" \
    sonarsource/sonar-scanner-cli
```

_Hopefully in SonarQube GUI you should end up seeing something like this_

![Successfully sonar scan for sonarqube](assets/sonar-scan-sonar-qube-result.png)

---

<br>

### Configuration

The following was done to configure _Pylint_ for `./server` _Python_ project:

```bash
# 1. Add _Pylint_ as dev dependency
poetry run pylint --generate-rcfile > .pylintrc

# 2. Create a _Pylint_ configuration file
poetry run pylint --generate-rcfile > .pylintrc

# 3. Run _Pylint_ via _Poetry_
poetry run pylint app
```