using OpenQA.Selenium;
using OpenQA.Selenium.Edge; // Or use ChromeDriver, etc.
using OpenQA.Selenium.Support.UI;
using HtmlAgilityPack;  // Equivalent to BeautifulSoup
using System;
using System.Collections.Generic;
using System.IO;
using System.Threading;

class Program
{
    static IWebDriver driver = new EdgeDriver(); // Change to ChromeDriver, FirefoxDriver if needed

    static void Main(string[] args)
    {
        try
        {
            NavigateWeb();
        }
        finally
        {
            TearDown();
        }
    }

    static void NavigateWeb()
    {
        Console.WriteLine("Preparing to parse: ");
        driver.Navigate().GoToUrl("https://www.msbar.org/lawyer-directory.aspx");
        driver.Manage().Timeouts().ImplicitWait = TimeSpan.FromSeconds(5);
        driver.Manage().Window.Maximize();

        while (true)
        {
            try
            {
                // Navigate to page 1: 0-2000 results
                Console.WriteLine("Navigating to page 1 results...");
                driver.FindElement(By.Id("radio5")).Click();
                driver.FindElement(By.Id("searchbox")).Click();
                driver.FindElement(By.Id("searchbox")).Clear();
                driver.FindElement(By.Id("searchbox")).SendKeys("MS");
                driver.FindElement(By.Id("searchbutton")).Click();
                Console.WriteLine("Resolving DOM...");

                // Grab data from page 1
                Console.WriteLine("Grabbing data from page 1...");
                GrabAllData();

                // Repeat for other pages (2 to 5) by updating the search box value
                for (int i = 2; i <= 5; i++)
                {
                    string pageInput = $"MS&page={i}&s={(i - 1) * 2000}";
                    driver.FindElement(By.Id("searchbox")).Clear();
                    driver.FindElement(By.Id("searchbox")).Click();
                    driver.FindElement(By.Id("searchbox")).SendKeys(pageInput);
                    driver.FindElement(By.Id("searchbutton")).Click();
                    Console.WriteLine($"Navigating to page {i}...");
                    GrabAllData();
                }

                Thread.Sleep(3000); // Wait for a while before navigating to next page
            }
            catch (NoSuchElementException)
            {
                Console.WriteLine("No such element found exception thrown");
            }
            catch (ElementNotVisibleException)
            {
                Console.WriteLine("Element not visible exception thrown");
            }
            catch (ElementNotSelectableException)
            {
                Console.WriteLine("Element not selectable exception thrown");
            }
            finally
            {
                break;
            }
        }
    }

    static void GrabAllData()
    {
        var pageSource = driver.PageSource;
        var doc = new HtmlDocument();
        doc.LoadHtml(pageSource);

        
        var data = new List<string>();
        var divs = doc.DocumentNode.SelectNodes("//section[@class='LawyerInformation cf']");

        if (divs != null)
        {
            foreach (var div in divs)
            {
                var lawyerInfo = new List<string>();
                var dataHolders = div.SelectNodes(".//div[@class='DataHolder']");
                if (dataHolders != null)
                {
                    foreach (var tag in dataHolders)
                    {
                        lawyerInfo.Add(tag.InnerText.Trim());
                    }

                    data.Add(string.Join(",", lawyerInfo));
                }
            }

            // Write to CSV
            File.AppendAllLines("data.csv", data);
        }
    }

    static void TearDown()
    {
        Console.WriteLine("Closing webdriver instance...");
        driver.Quit();
    }
}
