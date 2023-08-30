public class PriceCalculator {
    private Book book;
    private Integer quantity;
    private Double discountRate;
    private Double taxRate;
    
    public Double getTotal() {
        double price = ((book.getPrice() - book.getPrice() * discountRate) * this.quantity);
        return price * (1 + taxRate);
    }
}
