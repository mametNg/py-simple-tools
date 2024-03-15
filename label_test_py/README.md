# Print Label Test

Print Label Test is an application that supports the packing process at PT. Utac Manufacturing Services Indonesia, which aims to verify the printer that will be used whether the printed label results comply with the specified specifications or not.
Print test labels will be carried out before the production (packing) process begins.

## Preview

application display

![App Screenshot](https://raw.githubusercontent.com/mametNg/py-simple-tools/main/label_test_py/label-print/preview/application.png)

Inner label

![App Screenshot](https://raw.githubusercontent.com/mametNg/py-simple-tools/main/label_test_py/label-print/preview/inner_test_label.png)

Outer label

![App Screenshot](https://raw.githubusercontent.com/mametNg/py-simple-tools/main/label_test_py/label-print/preview/outer_test_label.png)

## Documentation

To be able to run this application until the label printing process requires additional applications, namely:

[BARTENDER DESIGNER](https://www.seagullscientific.com/support/downloads/) - Lincense required

[BARTENDER INTEGRATION BUILDER](https://www.seagullscientific.com/support/downloads/) - Lincense required

[BARTENDER GUIDES](https://support.seagullscientific.com/hc/en-us/categories/7750888437015-BarTender)

## Installation
#### Bartender
TaskList configuration

Open and edit config file "TaskList.btin" on folder bartender
```XML
<IntegrationFile Name="TaskList" Version="6" ID="7e66ac60-d8ba-4a9c-a3ad-0840d765529f">
  <ActionGroup Name="IntegrationFileActionGroup" ID="0e3903df-85ad-4622-9578-56be45120e3f" RunMethod="Sequential" MessagingEnabled="false">
    <Actions>
      <FileTriggerIntegration Name="Label Test" ID="97e77444-2ba8-434c-b95c-08f354657174" IgnoreErrors="true" DetectionMethod="Notification" Filter="*.csv" DetectionExtension="dat" LockedFileTimeout="30000">
        <ActionGroup ID="a778ec6f-0095-4acb-8742-6f40a019ab20" RunMethod="Sequential" MessagingEnabled="false">
          <Actions>
            <IntegrationCommandScriptAction Name="Print Command Script" ID="39b4c58f-7f5f-477f-9dd2-989e835fdb74" IgnoreErrors="true">
              <Script>
                <Value>%EventData%</Value>
              </Script>
              <BTCommandLineCredentials />
            </IntegrationCommandScriptAction>
          </Actions>
        </ActionGroup>
        <ScanFolder Path="C:\xampp\htdocs\python\label_test_py\label-print\trigger\" />
      </FileTriggerIntegration>
    </Actions>
  </ActionGroup>
  <Metadata>
    <Properties>
      <Properties Name="BuilderName" Type="System.String">
        <Value>TaskListToIntegrationFileConverter</Value>
      </Properties>
      <Properties Name="BuilderVersion" Type="System.Double">
        <Value>1</Value>
      </Properties>
      <Properties Name="MostRecentlyUsedVariables" Type="System.String">
        <Value>EventData</Value>
      </Properties>
      <Properties Name="SelectedDeploymentConfiguration" Type="System.String">
        <Value>Custom</Value>
      </Properties>
      <Properties Name="SelectedIntegration" Type="System.Int32">
        <Value>16</Value>
      </Properties>
      <Properties Name="SelectedOptionsPage" Type="System.String">
        <Value>0;0</Value>
      </Properties>
    </Properties>
  </Metadata>
  <SourcePath>C:\xampp\htdocs\python\label_test_py\bartender\TaskList.btin</SourcePath>
  <IsPrinting>false</IsPrinting>
  <IsPrintPreview>false</IsPrintPreview>
</IntegrationFile>
```
Change configuration

- in the ScanFolder element section, change the contents of the path attribute name according to the folder used to collect data sent from the label test application


#### Application
Install label_test_py with pip

```bash
  pip install -r requirements.txt
```    
## Running Tests

To run tests, run the following command

```bash
  python app.py
```

To run compile to exe, run the following command

```bash
  pyinstaller app.py --onefile --noconsole -i "assets/img/icon.ico"
```

