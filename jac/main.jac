walker generate_summary {
    has url;
    has anchor summary;
    can cl_summer.summarize;
    summary = cl_summer.summarize(text="none", url=url, sent_count=1);
    report summary;
}

walker generate_image {
    has text;
    can text_to_image.generate;
    has anchor generated_img;
    generated_img = text_to_image.generate(text=text);
    report generated_img;
}

walker init {
    summary =  spawn here walker::generate_summary(url="https://www.theverge.com/2023/5/2/23707140/motorola-edge-plus-2023-specs-price-features");
    generated_img = spawn here walker::generate_image(text=summary[0]);
}