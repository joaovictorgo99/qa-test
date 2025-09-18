describe('register', () => {
    beforeEach(() => {
        cy.visit("http://localhost:3000")
    })

    it('register an account', () => {
        cy.visit('http://localhost:3000/')
        cy.get('[data-test="signup"]').click()
        cy.get('[name="firstName"]').type("Rich")
        cy.get('[name="lastName"]').type("Guy")
        cy.get('[name="username"]').type("richg")
        cy.get('[name="password"').type("1234")
        cy.get('[name="confirmPassword"]').type("1234")
        cy.get('[data-test="signup-submit"]').click()
    })

    it('makes a first login to an account', () => {
        cy.get('[name="username"]').type("richg")
        cy.get('[name="password"]').type("1234")
        cy.get('[data-test="signin-submit"]').click()
        cy.get('[data-test="user-onboarding-dialog-title"]').contains("Get Started with Real World App")
        cy.get('[data-test="user-onboarding-next"]').click()
        cy.get('[name="bankName"]').type("Test Bank")
        cy.get('[name="routingNumber"]').type("123456789")
        cy.get('[name="accountNumber"]').type("123456789")
        cy.get('[data-test="bankaccount-submit"]').click()
        cy.get('[data-test="user-onboarding-dialog-title"]').contains("Finished")
        cy.get('[data-test="user-onboarding-next"]').click()
        cy.get('[data-test="nav-public-tab"]').contains("Everyone")
    })
})
