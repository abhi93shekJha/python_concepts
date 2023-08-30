public class InvoicePrinter {
    private Invoice invoice;
    private double total;

    public InvoicePrinter(Invoice invoice, double total) {
        this.invoice = invoice;
        this.total = total;
    }
    
    public void printInvoice() {
        System.out.println(invoice.getQuantity() + "x " + invoice.getBook().getName() + " " + invoice.getBook().getPrice() + "$");
        System.out.println("Discount Rate: " + invoice.getDiscountRate());
        System.out.println("Tax Rate: " + invoice.getTaxRate());
        System.out.println("Total: " + total);
    }
}
