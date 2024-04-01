def new_metamask(driver, account):
    """
    Creates a new MetaMask account and adds it to the browser.

    Args:
        driver (webdriver): The Selenium WebDriver instance.
        account (dict): The account to add.

    Returns:
        None
    """

    # Open the MetaMask extension.
    driver.get("chrome-extension://nkbihfbeogaeaoehlefnkodbefgpgknn/home.html")

    # Click the "Create a Wallet" button.
    driver.find_element_by_xpath("//button[text()='Create a Wallet']").click()

    # Accept the terms of service.
    driver.find_element_by_xpath("//button[text()='I Agree']").click()

    # Create a password for the account.
    driver.find_element_by_xpath("//input[@id='password']").send_keys(account["password"])

    # Confirm the password.
    driver.find_element_by_xpath("//input[@id='confirm-password']").send_keys(account["password"])

    # Click the "Create" button.
    driver.find_element_by_xpath("//button[text()='Create']").click()

    # Save the seed phrase.
    seed_phrase = driver.find_element_by_xpath("//div[@class='seed-phrase']").text
    with open("seed_phrase.txt", "w") as f:
        f.write(seed_phrase)

    # Click the "Next" button.
    driver.find_element_by_xpath("//button[text()='Next']").click()

    # Confirm the seed phrase.
    for word in seed_phrase.split(" "):
        driver.find_element_by_xpath(f"//button[text()='{word}']").click()

    # Click the "Confirm" button.
    driver.find_element_by_xpath("//button[text()='Confirm']").click()

    # Click the "All Done" button.
    driver.find_element_by_xpath("//button[text()='All Done']").click()

    # Add the account to the browser.
    driver.execute_script(
        """
        window.ethereum.request({
            method: 'wallet_addEthereumChain',
            params: [{
                chainId: '0x1',
                chainName: 'Ethereum Mainnet',
                nativeCurrency: {
                    name: 'Ether',
                    symbol: 'ETH',
                    decimals: 18
                },
                rpcUrls: ['https://www.example.com            }]
        });
        """
    )
    driver.execute_script(
        """
        window.ethereum.request({
            method: 'wallet_watchAsset',
            params: {
                type: 'ERC20',
                options: {
                    address: '0x6b175474e89094c44da98b954eedeac495271d0f',
                    symbol: 'DAI',
                    decimals: 18,
                    image: 'https://www.example.com                }
            }
        });
        """
    )

    # Import the private key into the account.
    driver.execute_script(
        """
        window.ethereum.request({
            method: 'wallet_importPrivateKey',
            params: ['0x%s']
        });
        """
        % account["private_key"]
    )

    # Refresh the page.
    driver.refresh()
