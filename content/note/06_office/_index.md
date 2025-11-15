---
title: "Office"
menuPre: '<i class="fab fa-microsoft"></i> ' 
weight: 7
---

## Install guide

1. Go to this website <https://config.office.com/deploymentsettings>
2. For **Office Suites**, choose **Office LTSC Standard 20XX - Volume License**
3. Check **Apps** you want to install
4. Click **Next**
5. **Select primary language**
6. Click **Next** twice
7. For **Upgrade options**, turn off **Uninstall any MSI versions of Office, including Visio and Project**
8. Click **Next** three times
9. Click **Finish**
10. Click **Export**
11. Choose **Office Open XML Formats**
12. Click **OK**
13. Check **I accept the terms in the license agreement**
14. Click **Export**
15. Go to this website <https://www.microsoft.com/en-us/download/details.aspx?id=49117>
16. Download **Office Deployment Tool**
17. Copy two downloaded files to a new folder name ```office``` in disk C
18. Open CMD as administrator
19. Run this command ```cd c:\office```
20. Then run this ```setup.exe /configure configuration.xml```