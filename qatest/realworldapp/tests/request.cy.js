describe('request', () => {
    it('makes a request', () => {
        cy.visit('http://localhost:3000/')
        cy.get('[name="username"]').type("richg")
        cy.get('[name="password"]').type("1234")
        cy.get('[data-test="signin-submit"]').click()
        cy.get('[data-test="nav-top-new-transaction"]').click()
        cy.get('[data-test="user-list-item-uBmeaz5pX"]').click()
        cy.get('[name="amount"]').type("1.99")
        cy.get('.MuiInputBase-root > [name="description"]').type("request")
        cy.get('[data-test="transaction-create-submit-request"]').click()
        cy.get('[data-test="new-transaction-return-to-transactions"]').click()
    })
})
