public class Invoice {
    private Book book;
    private Integer quantity;
    private Double discountRate;
    private Double taxRate;
    
    public Invoice(Book book, Integer quantity, Double discountRate, Double taxRate, double total) {
        this.book = book;
        this.quantity = quantity;
        this.discountRate = discountRate;
        this.taxRate = taxRate;
    }

    public Book getBook() {
        return this.book;
    }

    public Integer getQuantity() {
        return this.quantity;
    }


    public Double getDiscountRate() {
        return this.discountRate;
    }

    public Double getTaxRate() {
        return this.taxRate;
    }


    public void saveToFile(String filename) {
        // Creates a file with given name and writes the invoice
    }

}
