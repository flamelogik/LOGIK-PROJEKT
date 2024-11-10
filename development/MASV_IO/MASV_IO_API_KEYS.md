Name                                Type                          Required                  Description

name                                String                        Yes                       Name of the Portal to create.

subdomain                           String                        Yes                       Subdomain of the Portal to create.

message                             String                        No                        Message displayed on the Portal upload page.

has_access_code                     Boolean                       No                        Enable/disable access code for Portal page.

access_code                         String                        No                        Access code to be able to access Portal upload page.
                                                                                            Must be set if has_access_code is true.

active                              Boolean                       No                        Enable/disable Portal page.
                                                                                            Default is false.

logo_url                            String                        No                        URL for logo to be displayed on Portal page.

background_url                      String                        No                        URL for background image of the Portal page.

primary_color                       String                        No                        HTML hex code for primary color used on Portal page.

recipients                          Array of Strings              No                        Email(s) that will receive notifications for Portal uploads.

has_download_password               Boolean                       No                        Enable/disable download password for Portal packages.
                                                                                            Default is false.

download_password                   String                        No                        Password to protect download access on any package uploaded to this Portal.
                                                                                            Must be set if has_download_password is true.

custom_expiry_days                  Integer                       No                        Length of storage days for packages that belong to the Portal.
                                                                                            Must be from -1 to 65535.

cloud_connections                   Array of cloud connections    No                        Cloud connections attached to the Portal.
                                                                                            Must be set if configure_cloud_connections is true. See Cloud connect.

disable_upload_receipt              Boolean                       No                        Enable/disable the sending of a confirmation email to the uploader
                                                                                            Default is false.

custom_webhooks                     Array of custom webhooks      No                        Custom webhooks attached to the Portal.
                                                                                            See Custom webhooks.

tag                                 Tag                           No                        An optional tag object used to assign a tag to the new Portal.
                                                                                            When a Portal has a tag, all packages created on the Portal are assigned the Portal's tag.
                                                                                            See Tags.

access_level                        String                        No                        Portal access level, regular or private. Default is regular.

access_list                         Array of Strings              No                        User membership IDs with access to the private Portal and its received packages.
                                                                                            Leave it empty for regular Portals.

teamspace_id                        String                        No                        ID of the Teamspace that the Portal should be bound to.
                                                                                            To attach the Portal to a Team and not a Teamspace, either use the empty string or omit this object.

terms_of_service_enabled            Boolean                       No                        Enable/disable the display of the Terms of Service checkbox.
                                                                                            Default is false.

terms_of_service                    Terms of service              No                        Custom terms of service required to start collecting files.
                                                                                            If terms_of_service_enabled set to true this object cannot be empty or omitted.

package_size_restriction_enabled    Boolean                       No                        Enable/disable restrictions on the package size, as well as the number and size of files included in the Package.
                                                                                            If it is set to true then one or more of max_package_size, max_file_size, or max_file_count must be provided.
                                                                                            Default is false.

max_package_size                    Integer                       No                        The maximum Package size allowed for Users to input and save through the Portal.

max_file_size                       Integer                       No                        The maximum size, in bytes, of an individual file allowed for Users to input and save through the Portal.

max_file_count                      Integer                       No                        The maximum number of files allowed for the Portal upload.

file_type_restriction_enabled       Boolean                       No                        Enable/disable list of File types allowed for Users to upload.
                                                                                            If file_type_restriction_enabled set to true, this list cannot be empty or omitted. Default is false.

file_types                          Array of Strings              No                        File types allowed for upload only.
                                                                                            File type is presented as a file extension prefixed with a dot like ".mov" or ".mp4".

expiry_enabled                      Boolean                       No                        Enable/disable expiry for the Portal.
                                                                                            When enabled this will make the Portal unavailable for new uploads once the expiry datetime has passed.
                                                                                            Default is false.

expiry                              String                        No                        Date-time expiry for the Portal.
                                                                                            Default: 0001-01-01T00:00:00.000Z.
                                                                                            Accepted Format: ISO 8601.

package_name_format                 Package name format           No                        Accepted syntax for package names sent through this Portal.
                                                                                            MASV enforces this format only when package_name_format_enabled is true.
                                                                                            
package_name_format_enabled         Boolean                       No                        Enable/disable encorcement of package_name_format