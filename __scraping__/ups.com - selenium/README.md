Example with Selenium

- open page https://wwwapps.ups.com/WebTracking/OnlineTool
- accept cookie options
- switch to `Track by Reference`
- put reference number `w83139338`
- set dates `From` `01.11.2020` and `To` `07.02.2021` (US format: `11/01/2020`, `02/07/2021`)
- press button `Track`
- get values from page with result

Result:

```
track_number: xxxxxxxxxxxxxx2611
item: Delivered On:
item: Friday,  13.11.2020 at 19:10
item: Left At:
item: Front door
item: Received By:
item: DRIVER RELEASE
address: MIAMI,  FL  US 
hidden: podLoc = en_PL
hidden: lineData = Miami%5EFS%5EUS%5E20201113%5EFL%5E191044%5ED%5E-%5E-%5E-%5E-%5E-%5E-%5E-%5E-%5E-%5E-%5E-%5E-%5E-%5EMIAMI%5EUS%5E-%5E-%5E-%5EFL%5E11011%5E-%5E-%5E-%5E-%5E21b4%5E-%5EE10Y19%5E-%5EFront+door%5E1%5E-%5E-%5E0.40%5E20201108%5Etdts%5E-%5E-%5E-%5E11%5E-%5E-%5EE10Y19%5EUPS+Worldwide+Express+Saver%C2%AE%5E-%5ECN%5E-%5EDRIVER+RELEASE%5ED%5E-%5E-%5E-%5E1ZE10Y190401742611%5EKGS%5E-%5E-%5E-%5E-%5E-%5E-%5E1%5E-%5ES%5E-%5E-%5E-%5EN%5E-%5E0%5EN%5E0%5EDelivered%5E0%5E0%5E0%5E0%5E011%5E-%5E-%5E-%5E-%5ECGO%5E-%5E-%5E566%5E-%5E065%5Efalse%5E-%5E-%5E-%5E-%5E-%5E-%5E-%5E-%5Efalse%5Efalse%5Efalse%5Efalse%5E-%5EN%5E0%5E0%5E-%5E-%5EU%5E-%5E-%5E-%5E-%5E-%5E-%5E-%5E-%5E-%5E-%5E-%5E-%5E0%5E0%5E0%5E-%5E-%5E-%5E-%5E-%5E-%5E-%5E-%5E-%5E-%5E-%5E-%5E-%5E-%5E-%5E-%5E0%5E0%5E0%5E0%5E0%5Exxxxxxxxxxxxxx2611%5E1%5E-%5E1ZE10Y190401742611%5E%26returnapp%3Dtracking%26returnto%3Dhttps+3A+2F+2Fwwwapps.ups.com+2FWebTracking+2FprocessInputRequest+3Floc+3Den_PL+26tracknum+3D1ZE10Y190401742611%5E-%5E0%5E-%5E-%5E-%5E-%5E-%5E
hidden: retailLineData = null
hidden: refNumbers = 
hidden: Requester = 
hidden: lineItem = line1
hidden: tracknum = xxxxxxxxxxxxxx2611
hidden: podURL = https://wwwapps.ups.com/WebTracking
```
